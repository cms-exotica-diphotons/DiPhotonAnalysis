#!/usr/bin/env python

#
# Script to compute limits and make plots
# Runs support functions in MakePlots.py and MakeLimits.py
# Seth I. Cooper, U. Alabama
# November 2012
#
#   * Must set up CMSSW area and do cmsenv
#   * Must check out StatisticalTools/RooStatsRoutines package and then:
#     source $CMSSW_BASE/src/StatisticalTools/RooStatsRoutines/setup/setup/lxplus_standalone_setup.sh
#   * More instructions/notes can be found on the twiki page:
#     https://twiki.cern.ch/twiki/bin/view/CMS/ExoticaDiphotonResonance2012#Limit_Setting_Code_Instructions


import string
import os
import sys
import glob
import math
import array
import subprocess
import datetime
import itertools

# run root in batch
sys.argv.append('-b')
from ROOT import *
from MakePlots import *
from MakeLimits import *


# mapping of couplings/masses to halfWidths --> taken as input from fits
halfWidths0p01 = dict()
halfWidths0p01[750]  = 5.2041
halfWidths0p01[1000] = 6.50326
halfWidths0p01[1250] = 8.53237
halfWidths0p01[1500] = 10.0917
halfWidths0p01[1750] = 11.5976
halfWidths0p01[2000] = 13.6845
halfWidths0p01[3000] = 22.4852
# 0.05
halfWidths0p05 = dict()
halfWidths0p05[1750] = 13.7476
halfWidths0p05[2000] = 16.795
halfWidths0p05[2500] = 20.4539
halfWidths0p05[2750] = 22.7374
halfWidths0p05[3000] = 25.2982
# 0.1
halfWidths0p1 = dict()
halfWidths0p1[2250] = 26.3803
halfWidths0p1[2500] = 30.8038
halfWidths0p1[2750] = 35.9283
halfWidths0p1[3000] = 38.7399
halfWidths0p1[3250] = 41.8178
halfWidths0p1[3500] = 40.2991
# mapping of couplings/masses to crossSections --> taken from AN-12-305
# XXX: Update 2 Sep 2014 with 25k GEN Pythia cross sections
# 0.01
totalXSecs0p01 = dict()
totalXSecs0p01[750] = 1.003e-02
totalXSecs0p01[1000] = 1.958e-03
totalXSecs0p01[1250] = 5.045e-04 
totalXSecs0p01[1500] = 1.534e-04 
totalXSecs0p01[1750] = 5.195e-05 
totalXSecs0p01[2000] = 1.882e-05 
totalXSecs0p01[2250] = 7.203e-06 
totalXSecs0p01[2500] = 2.849e-06 
totalXSecs0p01[3000] = 4.586e-07
# 0.05
totalXSecs0p05 = dict()
totalXSecs0p05[1250] = 1.261e-02
totalXSecs0p05[1500] = 3.814e-03
totalXSecs0p05[1750] = 1.289e-03
totalXSecs0p05[2000] = 4.684e-04
totalXSecs0p05[2250] = 1.802e-04
totalXSecs0p05[2500] = 7.073e-05
totalXSecs0p05[2750] = 2.831e-05
totalXSecs0p05[3000] = 1.151e-05
# 0.1
totalXSecs0p1 = dict()
totalXSecs0p1[1500] = 1.518e-02
totalXSecs0p1[1750] = 5.131e-03
totalXSecs0p1[2000] = 1.872e-03
totalXSecs0p1[2250] = 7.194e-04
totalXSecs0p1[2500] = 2.861e-04
totalXSecs0p1[2750] = 1.151e-04
totalXSecs0p1[3000] = 4.684e-05
totalXSecs0p1[3250] = 1.925e-05
totalXSecs0p1[3500] = 7.751e-06



# for writing to log file+stdout
class MyTee():
  def __init__(self,logfile):
    self.stdout = sys.stdout
    self.logfile = open(logfile,'w')
  def write(self,txt):
    self.stdout.write(txt)
    self.logfile.write(txt)
    self.logfile.flush()
  def close(self):
    self.stdout.close()
    self.logfile.close()


def GetHalfWidth(coupling,mass):
  if coupling==0.01:
    dict = halfWidths0p01
  elif coupling==0.05:
    dict = halfWidths0p05
  elif coupling==0.1:
    dict = halfWidths0p1
  else:
    dict = dict()
  if mass in dict:
    return dict[mass]
  else:
    return -1
    #print 'GetHalfWidth: Coupling',coupling,'mass',mass,'not recognized; quitting'
    #exit()


def GetXSec(coupling,mass):
  if coupling==0.01:
    dict = totalXSecs0p01
  elif coupling==0.05:
    dict = totalXSecs0p05
  elif coupling==0.1:
    dict = totalXSecs0p1
  else:
    dict = dict()
  if mass in dict:
    return dict[mass]
  else:
    print 'GetXSec: Coupling',coupling,'mass',mass,'not recognized; quitting'
    exit()


def GetSignalFileName(template,channel):
  return template.format(ch=channel)


def FillKFactors(modelPointArray):
  myCoupling = modelPointArray[0].coupling
  massToKFactorDict = dict()
  with open(kFactorFile, 'r') as file:
    lines = file.readlines()
  i = 0
  while i < len(lines):
    line = lines[i]
    line.strip('\n')
    if "Coupling" in line:
      coupling = float(line.split('= ')[1])
      if coupling == myCoupling:
        break
    i+=1
  if i>=len(lines):
    print 'Could not find k-factors in file:',kFactorFile,'for coupling=',myCoupling
    return
  i+=2 # get past ----- line
  line = lines[i]
  while i < len(lines):
    if '--' in line:
      break
    lineSplit = line.split()
    massToKFactorDict[int(float(lineSplit[0]))] = float(lineSplit[1])
    i+=1
    line = lines[i]
  for mp in modelPointArray:
    mp.kFactor = massToKFactorDict[mp.mass]


# TODO: remove hardcoding; instead use list of couplings to run over
def DoLimitsAllPoints(cl95MacroPathAndName,doBatch,queueName,lumi,lumiErr,limitsFileName,limitsDirRel):
  if not os.path.isfile(optimizationFileName+'0p01.txt'):
    print
    print 'ERROR: Could not find optimization file: ',optimizationFileName+'0p01.txt'
    print '       Must run optimization first. Quiting.'
    exit(-1)
  if not os.path.isfile(optimizationFileName+'0p05.txt'):
    print
    print 'ERROR: Could not find optimization file: ',optimizationFileName+'0p05.txt'
    print '       Must run optimization first. Quiting.'
    exit(-1)
  if not os.path.isfile(optimizationFileName+'0p1.txt'):
    print
    print 'ERROR: Could not find optimization file: ',optimizationFileName+'0p1.txt'
    print '       Must run optimization first. Quiting.'
    exit(-1)
  print 'Run for coupling 0.01'
  with open(optimizationFileName+'0p01.txt', 'r') as file:
    lines = file.readlines()
    readModelPointsC0p01 = ReadFromLines(lines)
    FillKFactors(readModelPointsC0p01)
  print 'Run for coupling 0.05'
  with open(optimizationFileName+'0p05.txt', 'r') as file:
    lines = file.readlines()
    readModelPointsC0p05 = ReadFromLines(lines)
    FillKFactors(readModelPointsC0p05)
  print 'Run for coupling 0.1'
  with open(optimizationFileName+'0p1.txt', 'r') as file:
    lines = file.readlines()
    readModelPointsC0p1 = ReadFromLines(lines)
    FillKFactors(readModelPointsC0p1)
  # run for all
  limitsDir=os.getcwd()+'/'+limitsDirRel
  ComputeLimits(cl95MacroPathAndName,doBatch,queueName,lumi,lumiErr,readModelPointsC0p01+readModelPointsC0p05+readModelPointsC0p1,limitsDir,UseCombine)
  #subprocess.call(['mv','cls_plots',limitsOutputDir])


## TODO
# function to read in the coupling we ran over
#def ReadResultsAllPoints():
#  resultsByCoupling = {}
#  for c in couplingsToRunOver:
#    # make coupling string
#    couplingString = f(c)
#    with open(limitsFileName+couplingString+'.txt', 'r') as file:
#      readModelPoints = ReadFromFile(file)
#    resultsByCoupling[c] = readModelPoints
#  return resultsByCoupling

def DoMergeCheckAllPoints(limitsDir,limitsFileNameBase):
  if not os.path.isfile(optimizationFileName+'0p01.txt'):
    print
    print 'ERROR: Could not find optimization file: ',optimizationFileName+'0p01.txt'
    print '       Must run optimization first. Quiting.'
    exit(-1)
  if not os.path.isfile(optimizationFileName+'0p05.txt'):
    print
    print 'ERROR: Could not find optimization file: ',optimizationFileName+'0p05.txt'
    print '       Must run optimization first. Quiting.'
    exit(-1)
  if not os.path.isfile(optimizationFileName+'0p1.txt'):
    print
    print 'ERROR: Could not find optimization file: ',optimizationFileName+'0p1.txt'
    print '       Must run optimization first. Quiting.'
    exit(-1)
  # remove old merged limits files if they exist
  for coupling in [0.01,0.05,0.1]:
    couplingString = str(coupling).replace('.','p')
    fileName=limitsFileNameBase+couplingString+'.txt'
    if os.path.isfile(fileName):
      os.remove(fileName)
  print 'Run for coupling 0.01'
  with open(optimizationFileName+'0p01.txt', 'r') as file:
    lines = file.readlines()
    readModelPointsC0p01 = ReadFromLines(lines)
    FillKFactors(readModelPointsC0p01)
  ret1 = MergeLimitJobs(readModelPointsC0p01,limitsDir,limitsFileNameBase,UseCombine)
  print 'Run for coupling 0.05'
  with open(optimizationFileName+'0p05.txt', 'r') as file:
    lines = file.readlines()
    readModelPointsC0p05 = ReadFromLines(lines)
    FillKFactors(readModelPointsC0p05)
  ret2 = MergeLimitJobs(readModelPointsC0p05,limitsDir,limitsFileNameBase,UseCombine)
  print 'Run for coupling 0.1'
  with open(optimizationFileName+'0p1.txt', 'r') as file:
    lines = file.readlines()
    readModelPointsC0p1 = ReadFromLines(lines)
    FillKFactors(readModelPointsC0p1)
  ret3 = MergeLimitJobs(readModelPointsC0p1,limitsDir,limitsFileNameBase,UseCombine)
  if not (ret1 and ret2 and ret3):
    print 'Exiting here'
    exit(-1)


def DoPlotsAllPoints(lumi,rootFile,pathToTDRStyle):
  # set up tdrStyle
  gROOT.ProcessLine('.L '+pathToTDRStyle)
  gROOT.ProcessLine('setTDRStyle()')
  mLimObsByChan = {}
  mLimExpByChan = {}
  print 'DoPlotsAllPoints: Run for coupling 0.01'
  with open(limitsFileName+'0p01.txt', 'r') as file:
    readModelPoints0p01 = ReadFromFile(file)
  for ch in GetListOfChannels(readModelPoints0p01):
    mLimObsByChan[ch] = []
    mLimExpByChan[ch] = []
    modelPoints = [mp for mp in readModelPoints0p01 if mp.channel==ch]
    for plotObsLim in [True,False]:
      for useKfactor in [True,False]:
        PlotBands(modelPoints,plotObsLim,lumi,useKfactor,rootFile,plotsOutputDir)
    m0p01,xs,mExp0p01,xsE = GetMassLimit(modelPoints,False)
    mLimObsByChan[ch].append(m0p01)
    mLimExpByChan[ch].append(mExp0p01)
    print string.ljust('Coupling: '+str(modelPoints[0].coupling),14),
    print 'channel',ch
    print ' Observed limit mass: %0.2f'%m0p01
    print '                Expected limit mass: %0.2f'%mExp0p01
    print '                Observed XSec limit: %0.6f'%xs
    print '                Expected XSec limit: %0.6f'%xsE
  print 'mLimObsByChan:',mLimObsByChan
  # 0.05
  print 'DoPlotsAllPoints: Run for coupling 0.05'
  with open(limitsFileName+'0p05.txt', 'r') as file:
    readModelPoints0p05 = ReadFromFile(file)
  for ch in GetListOfChannels(readModelPoints0p05):
    modelPoints = [mp for mp in readModelPoints0p05 if mp.channel==ch]
    for plotObsLim in [True,False]:
      for useKfactor in [True,False]:
        PlotBands(modelPoints,plotObsLim,lumi,useKfactor,rootFile,plotsOutputDir)
    m0p05,xs,mExp0p05,xsE = GetMassLimit(modelPoints,False)
    mLimObsByChan[ch].append(m0p05)
    mLimExpByChan[ch].append(mExp0p05)
    print string.ljust('Coupling: '+str(modelPoints[0].coupling),14),
    print 'channel',ch
    print ' Observed limit mass: %0.2f'%m0p05
    print ' Expected limit mass: %0.2f'%mExp0p05
    print ' Observed XSec limit: %0.6f'%xs
    print ' Expected XSec limit: %0.6f'%xsE
  # 0.1
  print 'DoPlotsAllPoints: Run for coupling 0.1'
  with open(limitsFileName+'0p1.txt', 'r') as file:
    readModelPoints0p1 = ReadFromFile(file)
  for ch in GetListOfChannels(readModelPoints0p1):
    modelPoints = [mp for mp in readModelPoints0p1 if mp.channel==ch]
    for plotObsLim in [True,False]:
      for useKfactor in [True,False]:
        PlotBands(modelPoints,plotObsLim,lumi,useKfactor,rootFile,plotsOutputDir)
    m0p1,xs,mExp0p1,xsE = GetMassLimit(modelPoints,False)
    mLimObsByChan[ch].append(m0p1)
    mLimExpByChan[ch].append(mExp0p1)
    print string.ljust('Coupling: '+str(modelPoints[0].coupling),14),
    print 'channel',ch
    print ' Observed limit mass: %0.2f'%m0p1
    print ' Expected limit mass: %0.2f'%mExp0p1
    print ' Observed XSec limit: %0.6f'%xs
    print ' Expected XSec limit: %0.6f'%xsE
  # 2-D results plot
  for ch in GetListOfChannels(readModelPoints0p01):
    mLimObs = mLimObsByChan[ch]
    mLimExp = mLimExpByChan[ch]
    couplings = [0.01,0.05,0.1]
    CouplingVsMassPlot(couplings,mLimExp,mLimObs,False,rootFile,lumi,plotsOutputDir,ch)
  # FIXME extend for mutiple channels
  ## with KF
  #m0p01,xs,mExp0p01,xsE = GetMassLimit(readModelPoints0p01,True)
  #print string.ljust('Coupling: '+str(readModelPoints0p01[0].coupling),14),
  #print ' Observed limit mass: %0.2f'%m0p01
  #print '  (K-Factor)  Expected limit mass: %0.2f'%mExp0p01
  #print '  (K-Factor)  Observed XSec limit: %0.6f'%xs
  #print '  (K-Factor)  Expected XSec limit: %0.6f'%xsE
  ## 0.05
  #m0p05,xs,mExp0p05,xsE = GetMassLimit(readModelPoints0p05,True)
  #print string.ljust('Coupling: '+str(readModelPoints0p05[0].coupling),14),
  #print ' Observed limit mass: %0.2f'%m0p05
  #print '  (K-Factor)  Expected limit mass: %0.2f'%mExp0p05
  #print '  (K-Factor)  Observed XSec limit: %0.6f'%xs
  #print '  (K-Factor)  Expected XSec limit: %0.6f'%xsE
  ## 0.1
  #m0p1,xs,mExp0p1,xsE = GetMassLimit(readModelPoints0p1,True)
  #print string.ljust('Coupling: '+str(readModelPoints0p1[0].coupling),14),
  #print ' Observed limit mass: %0.2f'%m0p1
  #print '  (K-Factor)  Expected limit mass: %0.2f'%mExp0p1
  #print '  (K-Factor)  Observed XSec limit: %0.6f'%xs
  #print '  (K-Factor)  Expected XSec limit: %0.6f'%xsE
  ## 2-D results plot
  #mLimObs = [m0p01,m0p05,m0p1]
  #mLimExp = [mExp0p01,mExp0p05,mExp0p1]
  #couplings = [0.01,0.05,0.1]
  #CouplingVsMassPlot(couplings,mLimExp,mLimObs,True,rootFile,lumi,plotsOutputDir)
  #print 'PlotAllAcceptances'
  #PlotAllAcceptances([readModelPoints0p01,readModelPoints0p05,readModelPoints0p1],lumi,rootFile,plotsOutputDir)
  ## efficiencies for all couplings/masses on same axes
  #print 'PlotAllEfficiencies'
  #PlotAllEfficiencies([readModelPoints0p01,readModelPoints0p05,readModelPoints0p1],lumi,rootFile,plotsOutputDir)
  #PlotAllEfficienciesMScale([readModelPoints0p01,readModelPoints0p05,readModelPoints0p1], lumi, rootFile, plotsOutputDir)
  #PlotAllEfficienciesMRes([readModelPoints0p01,readModelPoints0p05,readModelPoints0p1],lumi,rootFile,plotsOutputDir)
  #PlotAllEfficienciesPileup([readModelPoints0p01,readModelPoints0p05,readModelPoints0p1],lumi,rootFile,plotsOutputDir)
  ## half widths
  #print 'PlotAllHalfWidths'
  #PlotAllHalfWidths([readModelPoints0p01,readModelPoints0p05,readModelPoints0p1],lumi,rootFile,plotsOutputDir)
  ## exp BG
  #print 'PlotAllExpBGs'
  #PlotAllExpBGs([readModelPoints0p01,readModelPoints0p05,readModelPoints0p1],lumi,rootFile,plotsOutputDir)
  ## limit plot for all couplings on same axes
  #print 'PlotAllBands'
  #for useKfactor in [False,True]:
  #  PlotAllBands([readModelPoints0p01,readModelPoints0p05,readModelPoints0p1],lumi,useKfactor,rootFile,plotsOutputDir)

def DoTablesAllPoints(lumi,limitsDir):
  with open(limitsFileName+'0p01.txt', 'r') as file:
    readModelPoints0p01 = ReadFromFile(file)
  # 0.05
  with open(limitsFileName+'0p05.txt', 'r') as file:
    readModelPoints0p05 = ReadFromFile(file)
  # 0.1
  with open(limitsFileName+'0p1.txt', 'r') as file:
    readModelPoints0p1 = ReadFromFile(file)
  # save original stdout; redirect to stdout+logfile
  origStdOut = sys.stdout
  sys.stdout = MyTee(limitsDir+'/tables.txt')
  # now make txt table output
  tableTitleString=string.ljust('Kmpl',6)+string.ljust('Mass',6)
  tableTitleString+=string.ljust('Channel',10)
  tableTitleString+=string.ljust('Window',11)
  tableTitleString+=string.ljust('Eff.',8)
  tableTitleString+=string.ljust('ExpSig.',9)
  tableTitleString+=string.center('ExpBkg.',41)+string.center('Obs.',10)
  tableTitleString+=string.center('ThXSec',10)+string.center('ExpLim.',12)
  tableTitleString+=string.center('ObsLim.',12)
  print
  print tableTitleString
  for ch in GetListOfChannels(readModelPoints0p01+readModelPoints0p05+readModelPoints0p1):
    modelPoints0p01 = [mp1 for mp1 in readModelPoints0p01 if mp1.channel==ch]
    modelPoints0p05 = [mp2 for mp2 in readModelPoints0p05 if mp2.channel==ch]
    modelPoints0p1 = [mp3 for mp3 in readModelPoints0p1 if mp3.channel==ch]
    for modelPoint in modelPoints0p01+modelPoints0p05+modelPoints0p1:
      print modelPoint.StringTableLine(lumi)
  # twiki table
  twikiTitleString='|* '+string.ljust('Coupling',9)+' *|* '+string.ljust('Mass [GeV]',10)+' *|* '
  twikiTitleString+='Channel *|* '
  twikiTitleString+='Mass Window *|* '
  twikiTitleString+=string.ljust('Efficiency',8)+' *|* '
  twikiTitleString+=string.center('Exp. Sig. Evts.',10)+' *|* '
  twikiTitleString+=string.center('Exp. Bkg. Evts.',17)+' *|* '+string.center('Obs. Data',10)+' *|* '
  twikiTitleString+=string.center('Exp. Lim. [pb]',13)+' *|* '
  twikiTitleString+=string.center('Obs. Lim. [pb]',13)+' *|'
  print
  print twikiTitleString
  for ch in GetListOfChannels(readModelPoints0p01+readModelPoints0p05+readModelPoints0p1):
    for modelPoint in modelPoints0p01+modelPoints0p05+modelPoints0p1:
      print modelPoint.TwikiTableLine(lumi)
  # twiki mass limits
  for ch in GetListOfChannels(readModelPoints0p01+readModelPoints0p05+readModelPoints0p1):
    modelPoints0p01 = [mp1 for mp1 in readModelPoints0p01 if mp1.channel==ch]
    modelPoints0p05 = [mp2 for mp2 in readModelPoints0p05 if mp2.channel==ch]
    modelPoints0p1 = [mp3 for mp3 in readModelPoints0p1 if mp3.channel==ch]
    twikiMassTitleString = '|* Coupling *|* Channel *|* Expected XSec Limit [pb] *|* Observed XSec Limit [pb] *|* Expected Mass Limit [GeV] *|* Observed Mass Limit [GeV] *|'
    twikiLine = ''
    massLimObs, xsLimObs, massLimExp, xsLimExp = GetMassLimit(modelPoints0p01,False)
    twikiLine+='| 0.01 | '+ch+' |'+str(round(xsLimExp,5))+' | '+str(round(xsLimObs,5))+' | '+str(int(massLimExp))+' | '+str(int(massLimObs))+' |\n'
    massLimObs, xsLimObs, massLimExp, xsLimExp = GetMassLimit(modelPoints0p05,False)
    twikiLine+='| 0.05 | '+ch+' |'+str(round(xsLimExp,5))+' | '+str(round(xsLimObs,5))+' | '+str(int(massLimExp))+' | '+str(int(massLimObs))+' |\n'
    massLimObs, xsLimObs, massLimExp, xsLimExp = GetMassLimit(modelPoints0p1,False)
    twikiLine+='| 0.1  | '+ch+' |'+str(round(xsLimExp,5))+' | '+str(round(xsLimObs,5))+' | '+str(int(massLimExp))+' | '+str(int(massLimObs))+' |\n'
    print
    print twikiMassTitleString
    print twikiLine
    print
  #print 'WITH K-FACTOR'
  #print twikiTitleString
  #for modelPoint in readModelPoints0p01+readModelPoints0p05+readModelPoints0p1:
  #  print modelPoint.TwikiTableLine(lumi)
  ## twiki mass limits
  #twikiMassTitleString = '|* Coupling *|* Expected XSec Limit [pb] *|* Observed XSec Limit [pb] *|* Expected Mass Limit [GeV] *|* Observed Mass Limit [GeV] *|'
  #twikiLine = ''
  #massLimObs, xsLimObs, massLimExp, xsLimExp = GetMassLimit(readModelPoints0p01,True)
  #twikiLine+='| 0.01 | '+str(round(xsLimExp,5))+' | '+str(round(xsLimObs,5))+' | '+str(int(massLimExp))+' | '+str(int(massLimObs))+' |\n'
  #massLimObs, xsLimObs, massLimExp, xsLimExp = GetMassLimit(readModelPoints0p05,True)
  #twikiLine+='| 0.05 | '+str(round(xsLimExp,5))+' | '+str(round(xsLimObs,5))+' | '+str(int(massLimExp))+' | '+str(int(massLimObs))+' |\n'
  #massLimObs, xsLimObs, massLimExp, xsLimExp = GetMassLimit(readModelPoints0p1,True)
  #twikiLine+='| 0.1  | '+str(round(xsLimExp,5))+' | '+str(round(xsLimObs,5))+' | '+str(int(massLimExp))+' | '+str(int(massLimObs))+' |\n'
  #print
  #print twikiMassTitleString
  #print twikiLine
  ## latex table
  ## k, mass, windowRange, sigEff, expSigEvts, expBgEvts, obs
  #print
  #print
  #print '\\begin{table}[htpb]\n\t\\begin{center}'
  #print '\t\t\\begin{tabular}{ccccccc}\n\t\t\\hline'
  #print '\t\t$\\tilde{k}$ & $M_1$ & Window & Sig. Eff. & Exp. Sig. Evts. & Exp. Bg. Evts. & Obs. \\\\'
  #print '\t\t\\hline'
  #for modelPoint in readModelPoints0p01+readModelPoints0p05+readModelPoints0p1:
  #  print modelPoint.LatexTableLine(lumi)
  #print '\t\t\\hline'
  #print '\t\t\\end{tabular}'
  #captionLine="\t\t\\caption[Event Yields]{Event yields of signal and data after selection.  "
  #captionLine+="The columns show: coupling ``$\\tilde{k}$'', graviton mass ``$M_1$'' in GeV, mass window range ``Window'' in GeV, "
  #captionLine+="signal efficiency ``Sig. Eff.'', expected number of signal events ``Exp. Sig. Evts.'', "
  #captionLine+="expected number of background events and error ``Exp. Bg. Evts.'', and observed data events ``Obs.''.}"
  #print captionLine
  #print '\t\\label{table:eventYields}'
  #print '\t\\end{center}'
  #print '\\end{table}'
  ## next table -- limits
  #print
  #print
  #print '\\begin{table}[htpb]\n\t\\begin{center}'
  #print '\t\t\\begin{tabular}{ccc}\n\t\t\\hline'
  #print '\t\t\t$\\tilde{k}$ & $\sigma$ & $M_1$ \\\\'
  #print '\t\t\t\\hline'
  ## TODO remove hardcoding of couplings to run over
  ## 0.01
  #latexLine='\t\t\t'+'0.01'+' & '
  #massLimObs, xsLimObs, massLimExp, xsLimExp = GetMassLimit(readModelPoints0p01,False)
  #latexLine+='%.5f'%xsLimObs+' & '
  #latexLine+=str(int(massLimObs))
  #latexLine+=' \\\\'
  #print latexLine
  ## 0.05
  #latexLine='\t\t\t'+'0.05'+' & '
  #massLimObs, xsLimObs, massLimExp, xsLimExp = GetMassLimit(readModelPoints0p05,False)
  #latexLine+='%.5f'%xsLimObs+' & '
  #latexLine+=str(int(massLimObs))
  #latexLine+=' \\\\'
  #print latexLine
  ## 0.1
  #latexLine='\t\t\t'+'0.1'+' & '
  #massLimObs, xsLimObs, massLimExp, xsLimExp = GetMassLimit(readModelPoints0p1,False)
  #latexLine+='%.5f'%xsLimObs+' & '
  #latexLine+=str(int(massLimObs))
  #latexLine+=' \\\\'
  #print latexLine
  #print '\t\t\t\\hline'
  #print '\t\t\\end{tabular}'
  #captionLine="\t\t\\caption[Limit results]{ Limit results from the observed data. "
  #captionLine+="The columns show: coupling ``$\\tilde{k}$'', observed 95\% confidence level upper limit on the graviton cross section in pb, "
  #captionLine+="and the observed 95\% confidence level lower limit on the graviton mass ``$M_1$'' in GeV. }"
  #print captionLine
  #print '\t\\label{table:limitResults}'
  #print '\t\\end{center}'
  #print '\\end{table}'
  ## next table -- limits with K-FACTOR
  #print
  #print
  #print '% Limits with signal k-factor applied'
  #print '\\begin{table}[htpb]\n\t\\begin{center}'
  #print '\t\t\\begin{tabular}{ccc}\n\t\t\\hline'
  #print '\t\t\t$\\tilde{k}$ & $\sigma$ & $M_1$ \\\\'
  #print '\t\t\t\\hline'
  ## TODO remove hardcoding of couplings to run over
  ## 0.01
  #latexLine='\t\t\t'+'0.01'+' & '
  #massLimObs, xsLimObs, massLimExp, xsLimExp = GetMassLimit(readModelPoints0p01,True)
  #latexLine+='%.5f'%xsLimObs+' & '
  #latexLine+=str(int(massLimObs))
  #latexLine+=' \\\\'
  #print latexLine
  ## 0.05
  #latexLine='\t\t\t'+'0.05'+' & '
  #massLimObs, xsLimObs, massLimExp, xsLimExp = GetMassLimit(readModelPoints0p05,True)
  #latexLine+='%.5f'%xsLimObs+' & '
  #latexLine+=str(int(massLimObs))
  #latexLine+=' \\\\'
  #print latexLine
  ## 0.1
  #latexLine='\t\t\t'+'0.1'+' & '
  #massLimObs, xsLimObs, massLimExp, xsLimExp = GetMassLimit(readModelPoints0p1,True)
  #latexLine+='%.5f'%xsLimObs+' & '
  #latexLine+=str(int(massLimObs))
  #latexLine+=' \\\\'
  #print latexLine
  #print '\t\t\t\\hline'
  #print '\t\t\\end{tabular}'
  #captionLine="\t\t\\caption[Limit results]{ Limit results from the observed data with signal k-factors applied. "
  #captionLine+="The columns show: coupling ``$\\tilde{k}$'', observed 95\% confidence level upper limit on the graviton cross section in pb, "
  #captionLine+="and the observed 95\% confidence level lower limit on the graviton mass ``$M_1$'' in GeV. }"
  #print captionLine
  #print '\t\\label{table:limitResultsKFactor}'
  #print '\t\\end{center}'
  #print '\\end{table}'
  # reset stdout back to original
  sys.stdout = origStdOut
  

def DoOptimizeAllPoints(optimizationPlotFile):
  global modelPointsC0p01
  global modelPointsC0p05
  global modelPointsC0p1
  # configurable options for optimization
  maxWindowRange = 600 # GeV
  useAsymmWindow = False
  useSSB = True
  # save original stdout; redirect to stdout+logfile
  #origStdOut = sys.stdout
  #sys.stdout = MyTee(optimizationOutputDir+'/log.txt')
  print 'Run for coupling 0.01'
  colorIndex = 2 #TODO add this into modelpoint itself?
  with open(optimizationFileName+'0p01.txt', 'w') as file:
    modelPointsC0p01 = OptimizeSignalMassWindows(
        modelPointsC0p01,lumi,useAsymmWindow,useSSB,maxWindowRange,file,optimizationPlotFileNameTemplate,optimizationPlotFile,colorIndex,optimizationOutputDir,extraWindowMargin)
  print 'Run for coupling 0.05'
  colorIndex = 4
  with open(optimizationFileName+'0p05.txt', 'w') as file:
    modelPointsC0p05 = OptimizeSignalMassWindows(
        modelPointsC0p05,lumi,useAsymmWindow,useSSB,maxWindowRange,file,optimizationPlotFileNameTemplate,optimizationPlotFile,colorIndex,optimizationOutputDir,extraWindowMargin)
  print 'Run for coupling 0.1'
  colorIndex = 8
  with open(optimizationFileName+'0p1.txt', 'w') as file:
    modelPointsC0p1 = OptimizeSignalMassWindows(
        modelPointsC0p1,lumi,useAsymmWindow,useSSB,maxWindowRange,file,optimizationPlotFileNameTemplate,optimizationPlotFile,colorIndex,optimizationOutputDir,extraWindowMargin)
  # make multigraphs for all masses/couplings/channels
  # find channels
  modelPointArray = modelPointsC0p01+modelPointsC0p05+modelPointsC0p1
  channels = []
  for mp in modelPointArray:
    if not mp.channel in channels:
      channels.append(mp.channel)
  for ch in channels:
    MakeOptHalfWindowVsMassMultigraph(optimizationPlotFile,ch)
    MakeOptMassWindowsVsMassMultiGraph(optimizationPlotFile,ch)
    MakeOptSSBValueVsMassMultigraph(optimizationPlotFile,ch)
    #FIXME add channel
    ## print wiki-style table with links to plots (made/copied later by plotting script)
    #print 'Twiki-style table of mass windows'
    #print
    #print '| *Coupling* | *Mass (GeV)* | *Mass Window Low* | *Mass Window High* | *Mass Window Half-Width* | *Optimization Plot* | *PDF* |'
    #for mp in modelPointsC0p01:
    #  print '|',mp.coupling,'|',mp.mass,'|',mp.optMassWindowLow,'|',mp.optMassWindowHigh,'|',(mp.optMassWindowHigh-mp.optMassWindowLow)/2+0.5,'|',
    #  print '<a href="http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/ssbOpt_k0p01_m'+str(mp.mass)+'.png"><img src="http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/ssbOpt_k0p01_m'+str(mp.mass)+'.png" alt="optimization_K0p01_m'+str(mp.mass)+'" width="400" /></a>|<a href=http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/ssbOpt_k0p01_m'+str(mp.mass)+'.pdf>PDF Version</a>|'
    #print '| |||||'
    #for mp in modelPointsC0p05:
    #  print '|',mp.coupling,'|',mp.mass,'|',mp.optMassWindowLow,'|',mp.optMassWindowHigh,'|',(mp.optMassWindowHigh-mp.optMassWindowLow)/2+0.5,'|',
    #  print '<a href="http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/ssbOpt_k0p05_m'+str(mp.mass)+'.png"><img src="http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/ssbOpt_k0p05_m'+str(mp.mass)+'.png" alt="optimization_K0p05_m'+str(mp.mass)+'" width="400" /></a>|<a href=http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/ssbOpt_k0p05_m'+str(mp.mass)+'.pdf>PDF Version</a>|'
    #print '| |||||'
    #for mp in modelPointsC0p1:
    #  print '|',mp.coupling,'|',mp.mass,'|',mp.optMassWindowLow,'|',mp.optMassWindowHigh,'|',(mp.optMassWindowHigh-mp.optMassWindowLow)/2+0.5,'|',
    #  print '<a href="http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/ssbOpt_k0p1_m'+str(mp.mass)+'.png"><img src="http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/ssbOpt_k0p1_m'+str(mp.mass)+'.png" alt="optimization_K0p1_m'+str(mp.mass)+'" width="400" /></a>|<a href=http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/ssbOpt_k0p1_m'+str(mp.mass)+'.pdf>PDF Version</a>|'
    ## print out signal/background mass window plot code for twiki
    #print 'Twiki-style table of signal/background mass plot'
    #print '| *Coupling* | *Mass (!GeV)* | *Plot* | *PDF* |'
    #for mp in modelPointsC0p01:
    #  print '|0.01|',mp.mass,'|',
    #  print '<a href="http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/signalBackgroundOptWindows_k0p01_m'+str(mp.mass)+'.png"><img src="http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/signalBackgroundOptWindows_k0p01_m'+str(mp.mass)+'.png" alt="optimization_K0p01_m'+str(mp.mass)+'" width="600" /></a>|<a href=http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/signalBackgroundOptWindows_k0p01_m'+str(mp.mass)+'.pdf>PDF Version</a>|'
    #print '| ||||'
    #for mp in modelPointsC0p05:
    #  print '|0.05|',mp.mass,'|',
    #  print '<a href="http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/signalBackgroundOptWindows_k0p05_m'+str(mp.mass)+'.png"><img src="http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/signalBackgroundOptWindows_k0p05_m'+str(mp.mass)+'.png" alt="optimization_K0p05_m'+str(mp.mass)+'" width="600" /></a>|<a href=http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/signalBackgroundOptWindows_k0p05_m'+str(mp.mass)+'.pdf>PDF Version</a>|'
    #print '| ||||'
    #for mp in modelPointsC0p1:
    #  print '|0.1|',mp.mass,'|',
    #  print '<a href="http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/signalBackgroundOptWindows_k0p1_m'+str(mp.mass)+'.png"><img src="http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/signalBackgroundOptWindows_k0p1_m'+str(mp.mass)+'.png" alt="optimization_K0p1_m'+str(mp.mass)+'" width="600" /></a>|<a href=http://scooper.web.cern.ch/scooper/exoDiPhotons/twikiPlots/signalBackgroundOptWindows_k0p1_m'+str(mp.mass)+'.pdf>PDF Version</a>|'
  # reset stdout back to original
  #sys.stdout = origStdOut


def DoOptimizationPlots(optimizationRootFile):
  # toggle plot s/sqrt(b) off
  MakeOptGraphImages(optimizationRootFile,optimizationPlotFileNameTemplate,optimizationOutputDir,modelPointsC0p01+modelPointsC0p05+modelPointsC0p1,True)
  # above takes a lot of time--many points
  # do images
  MakeOptMassWindowVsMassImages(optimizationRootFile,optimizationOutputDir,channels)
  MakeSmoothedMassWindowVsMassImages(optimizationRootFile,optimizationOutputDir,channels)
  MakeOptSSBVsMassImages(optimizationRootFile, optimizationOutputDir, channels)
  MakeOptMassWindowSignalBackgroundImages(optimizationRootFile,optimizationOutputDir,modelPointsC0p01+modelPointsC0p05+modelPointsC0p1)


#def DoCalculateYieldsAllPoints():
#  print 'Yields: Run for coupling 0.01'
#  with open(optimizationFileName+'0p01.txt', 'w') as file:
#    CalculateYieldsForMassRanges(rootFileLocationDataFake, rootFileBackgroundMC, modelPointsC0p01, lumi, 3, file)
#  print 'Yields: Run for coupling 0.05'
#  with open(optimizationFileName+'0p05.txt', 'w') as file:
#    CalculateYieldsForMassRanges(rootFileLocationDataFake, rootFileBackgroundMC, modelPointsC0p05, lumi, 3, file)
#  print 'Yields: Run for coupling 0.1'
#  with open(optimizationFileName+'0p1.txt', 'w') as file:
#    CalculateYieldsForMassRanges(rootFileLocationDataFake, rootFileBackgroundMC, modelPointsC0p1, lumi, 3, file)


def GetConfigurationString():
  configString='-----------------------------------------------\n'+'Running with configuration:'+'\n'
  configString+='lumi='+str(lumi)+'\n'
  configString+='lumiErr='+str(lumiErr)+'\n'+'-----------------------------------------------\n'
  configString+='signalPoints K0p01='+str(masses0p01)+'\n'
  configString+='signalPoints K0p05='+str(masses0p05)+'\n'
  configString+='signalPoints K0p1='+str(masses0p1)+'\n'
  configString+='extraWindowMargin='+str(extraWindowMargin)+'\n'
  configString+='K-factor file='+kFactorFile+'\n'
  # overall systematics
  configString+='SigPUSyst='+str(SigPUSyst)+'\n'
  configString+='SigScaleFactorSystOneGamma='+str(SigScaleFactorSystOneGamma)+'\n'
  configString+='SigPtSFSystOneGamma='+str(SigPtSFSystOneGamma)+'\n'
  configString+='BGSystsFromHists'+'\n'+'-----------------------------------------------\n'
  configString+='optimizationOutputDir='+optimizationOutputDir+'\n'
  configString+='limitsOutputDir='+limitsOutputDir+'\n'
  configString+='limitsFileNameBase='+limitsFileNameBase+'\n'
  configString+='optimizationFileNameBase='+optimizationFileNameBase+'\n'+'-----------------------------------------------\n'
  return configString


def Usage():
  print 'Usage: python RunLimitsAndPlots.py [arg] where arg can be:'
  print '    1) optimize      --> Calculate optimal inv. mass windows using histograms in root files (from CreateHistogramFiles).'
  print '    2) limits        --> Compute limits for all model points.'
  print '    3) mergeLimits   --> Merge/check limit results for all model points. Run after batch jobs done.  Also makes plots and tables.'
  print '    plots         --> Read limit results from text files and make limit plots.'
  print '    tables        --> Read limit results from text files and make results tables (text/latex/twiki).'
  print '    optimizePlots --> Print optimization graphs as images (use after optimize has been run; done automatically by default).'
  print '    yields        --> Calculate event yields from histograms in root files (from CreateHistogramFiles).'
  print
  print 'Typically, one first runs optimize, then limits, then mergeLimits (after batch jobs are done if using batch submission).'
  print 'This will calculate all the results and make all the plots and tables.'




#
#
# RUN
#
gROOT.Reset()
# get path to tdrStyle script (should always be in LimitScripts, but we don't hardcode it anyway)
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
pathToTDRStyle = dname+'/tdrStyle.C'
# Define RooStats macro path and name
cl95MacroPath = os.environ['CMSSW_BASE']+'/src/StatisticalTools/RooStatsRoutines/root/'
cl95MacroName = 'roostats_cl95.C'


###################################################################################################
# Configurable stuff here
###################################################################################################
now = datetime.datetime.now()
Date = now.strftime("%b%d")
#outputDirBase = Date.lower()+'_symmWindowSSBOpt_loosePFID_test'
outputDirBase = 'aug20_symmWindowSSBOpt_loosePFID_test'
optimizationOutputDir = outputDirBase+'_optimization'
limitsOutputDir = outputDirBase+'_limits'
plotsOutputDir = outputDirBase+'_plots'
# limit results file base name
limitsFileNameBase = 'limits_k_'
limitsFileName = limitsOutputDir+'/'+limitsFileNameBase
limitsPlotFileName = limitsOutputDir+'/plots.root'
# optimization results file base name
optimizationFileNameBase = 'optimization_k_'
optimizationFileName = optimizationOutputDir+'/'+optimizationFileNameBase
optimizationPlotFileNameTemplate = optimizationOutputDir+'/plots_{mass}_{coup}_{chan}.root'
optimizationPlotFileName = optimizationOutputDir+'/plots.root'
# location of signal root files from Andrew
signalRootFilePath = '/afs/cern.ch/work/a/abuccill/public/forSeth/RSHistogramsForLimits/'
# location of data/fake root files from CreateHistogramFiles code
dataRootFilePath = '/afs/cern.ch/work/c/charaf/public/ForSeth/EndcapLimitTest2012/'
# location of backgroundMC root files from CreateHistogramFiles code
backgroundRootFilePath = '/afs/cern.ch/work/c/charaf/public/ForSeth/EndcapLimitTest2012/'
# k-factors to compute mass limit (optimization always done with k-factor=1)
kFactorFile = 'RS-KF-LHC-8TeV-y1.4442-ptcut80.dat'
# launch limit-setting jobs on lxbatch
DoBatch = False
QueueName = '8nh'
UseCombine = True
# use extra window margin to minimize mScale/mRes systematic effects on signal
extraWindowMargin = 0.00 # fraction to expand window by, e.g., 0.01 --> expand edges by 1%
# Declarations of Lumi and model points to consider -- must have xsec, etc. defined above
lumi = 19048.0
lumiErr = lumi*0.026
#masses0p01 = [750,1000,1250,1500,1750,2000,2250,2500,3000]
#masses0p05 = [1250,1500,1750,2000,2250,2500,2750,3000]
#masses0p1 = [1500,1750,2000,2250,2500,2750,3000,3250,3500]
#XXX SIC FIXME kick out 3500 for now (need even coarser binning to have nonzero background)
masses0p1 = [1500,1750,2000,2250,2500,2750,3000,3250]
# also 3000 has problems with the limits
masses0p01 = [750,1000,1250,1500,1750,2000,2250,2500]
masses0p05 = [1250,1500,1750,2000,2250,2500,2750]
channels = ['BB','BE','EB','EE']
##XXX SIC TEST
##channels = ['BB','BE']
#masses0p01 = [750,1000,1250]
#masses0p05 = [1250,1500,1750]
#masses0p1 = [1500,1750,2000]
#masses0p01 = [750]
#channels = ['BB']

configString = GetConfigurationString()
print configString
# to print the func
print 'SigPDFSystFunc:'
SigPDFSystFunc.Print()
print '----------------------------------------------- End of configuration info'

# List signal histogram file template; rest of quantities are filled from functions (xsec, width, etc.) or histograms in the files
# initialize signal points
signalFilenameTemplate = signalRootFilePath+'rsg_diphotonMinv_scaled_histograms_{chan}.root'
bgFilenameTemplate = backgroundRootFilePath+'{chan}histograms_TotalBackground.root'
dataFilenameTemplate = dataRootFilePath+'{chan}histograms_ExoDiPhotonAnalyzer_LooseCSEVEndcaps_DataABCD.root'
modelPointsC0p01 = []
modelPointsC0p05 = []
modelPointsC0p1 = []
# loop over the 4 channels
for ch in channels:
  # setup k=0.01
  for mass in masses0p01:
    k = 0.01
    modelPointsC0p01.append(ModelPoint(coupling=k,mass=mass,totalXSec=GetXSec(k,mass),halfWidth=GetHalfWidth(k,mass),
      fileName=signalFilenameTemplate.format(chan=ch),bgFileName=bgFilenameTemplate.format(chan=ch),
      dFileName=dataFilenameTemplate.format(chan=ch),channel=ch))
    #print 'added modelpoint:',
    #modelPointsC0p01[-1].Print()
  # setup k=0.05
  for mass in masses0p05:
    k = 0.05
    modelPointsC0p05.append(ModelPoint(coupling=k,mass=mass,totalXSec=GetXSec(k,mass),halfWidth=GetHalfWidth(k,mass),
      fileName=signalFilenameTemplate.format(chan=ch),bgFileName=bgFilenameTemplate.format(chan=ch),
      dFileName=dataFilenameTemplate.format(chan=ch),channel=ch))
  # setup k=0.1
  for mass in masses0p1:
    k = 0.1
    modelPointsC0p1.append(ModelPoint(coupling=k,mass=mass,totalXSec=GetXSec(k,mass),halfWidth=GetHalfWidth(k,mass),
      fileName=signalFilenameTemplate.format(chan=ch),bgFileName=bgFilenameTemplate.format(chan=ch),
      dFileName=dataFilenameTemplate.format(chan=ch),channel=ch))



# Parse arguments
if len(sys.argv)==1:
  Usage()
  sys.exit()
elif sys.argv[1]=='optimizePlots':
  print 'optimizePlots: print plot images from optimization'
  rootFile = TFile(optimizationPlotFileName,'update')
  DoOptimizationPlots(optimizationPlotFile)
  if not os.path.isdir(plotsOutputDir):
    os.mkdir(plotsOutputDir)
  with open(optimizationFileName+'0p01.txt', 'r') as file:
    lines = file.readlines()
    readModelPointsC0p01 = ReadFromLines(lines)
    FillKFactors(readModelPointsC0p01)
  with open(optimizationFileName+'0p05.txt', 'r') as file:
    lines = file.readlines()
    readModelPointsC0p05 = ReadFromLines(lines)
    FillKFactors(readModelPointsC0p05)
  with open(optimizationFileName+'0p1.txt', 'r') as file:
    lines = file.readlines()
    readModelPointsC0p1 = ReadFromLines(lines)
    FillKFactors(readModelPointsC0p1)
  PlotAllAcceptances([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,optimizationPlotFileNameTemplate,plotsOutputDir)
  #PlotAllAcceptancesMassWindows([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,rootFile,plotsOutputDir)
  PlotAllEfficiencies([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,optimizationPlotFileNameTemplate,plotsOutputDir)
  PlotAllEfficienciesMScale([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,optimizationPlotFileNameTemplate,plotsOutputDir)
  PlotAllEfficienciesMRes([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,optimizationPlotFileNameTemplate,plotsOutputDir)
  PlotAllEfficienciesPileup([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,optimizationPlotFileNameTemplate,plotsOutputDir)
  #PlotAllEfficienciesMScaleEffAcc([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,rootFile,plotsOutputDir)
elif sys.argv[1]=='effAccPlots':
  print 'effAccPlots: make efficiency and acceptance plots (inc. systematics plots)'
  rootFile = TFile(optimizationPlotFileName,'update')
  if not os.path.isdir(plotsOutputDir):
    os.mkdir(plotsOutputDir)
  with open(optimizationFileName+'0p01.txt', 'r') as file:
    lines = file.readlines()
    readModelPointsC0p01 = ReadFromLines(lines)
    FillKFactors(readModelPointsC0p01)
  with open(optimizationFileName+'0p05.txt', 'r') as file:
    lines = file.readlines()
    readModelPointsC0p05 = ReadFromLines(lines)
    FillKFactors(readModelPointsC0p05)
  with open(optimizationFileName+'0p1.txt', 'r') as file:
    lines = file.readlines()
    readModelPointsC0p1 = ReadFromLines(lines)
    FillKFactors(readModelPointsC0p1)
  PlotAllAcceptances([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,optimizationPlotFile,plotsOutputDir)
  #PlotAllAcceptancesMassWindows([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,rootFile,plotsOutputDir)
  PlotAllEfficiencies([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,optimizationPlotFile,plotsOutputDir)
  PlotAllEfficienciesMScale([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,optimizationPlotFile,plotsOutputDir)
  PlotAllEfficienciesMRes([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,optimizationPlotFile,plotsOutputDir)
  PlotAllEfficienciesPileup([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,optimizationPlotFile,plotsOutputDir)
  #PlotAllEfficienciesMScaleEffAcc([readModelPointsC0p01,readModelPointsC0p05,readModelPointsC0p1],lumi,rootFile,plotsOutputDir)
elif sys.argv[1]=='optimize':
  print 'optimize: OptimizeSignalMassWindows'
  print 'warning: will overwrite file',optimizationPlotFileName,'if it already exists.'
  if not os.path.isdir(optimizationOutputDir):
    os.mkdir(optimizationOutputDir)
  with open(optimizationOutputDir+'/config.txt', 'w') as file:
    file.write(configString)
  # recreate tfile for optimize step
  rootFile = TFile(optimizationPlotFileName,'recreate')
  DoOptimizeAllPoints(rootFile)
  DoOptimizationPlots(rootFile)
  if not os.path.isdir(plotsOutputDir):
    os.mkdir(plotsOutputDir)
  PlotAllAcceptances([modelPointsC0p01,modelPointsC0p05,modelPointsC0p1],lumi,rootFile,plotsOutputDir)
  PlotAllAcceptancesMassWindows([modelPointsC0p01,modelPointsC0p05,modelPointsC0p1],lumi,rootFile,plotsOutputDir)
  PlotAllEfficiencies([modelPointsC0p01,modelPointsC0p05,modelPointsC0p1],lumi,rootFile,plotsOutputDir)
  PlotAllEfficienciesMScale([modelPointsC0p01,modelPointsC0p05,modelPointsC0p1],lumi,rootFile,plotsOutputDir)
  PlotAllEfficienciesMRes([modelPointsC0p01,modelPointsC0p05,modelPointsC0p1],lumi,rootFile,plotsOutputDir)
  PlotAllEfficienciesPileup([modelPointsC0p01,modelPointsC0p05,modelPointsC0p1],lumi,rootFile,plotsOutputDir)
# no longer maintained in 2015
#elif sys.argv[1]=='yields':
#  print 'yields: CalculateYieldsForMassRanges'
#  if not os.path.isdir(optimizationOutputDir):
#    os.mkdir(optimizationOutputDir)
#  with open(optimizationOutputDir+'/config.txt', 'w') as file:
#    file.write(configString)
#  rootFile = TFile(optimizationPlotFileName,'recreate')
#  DoCalculateYieldsAllPoints()
#  if not os.path.isdir(plotsOutputDir):
#    os.mkdir(plotsOutputDir)
#  PlotAllAcceptances([modelPointsC0p01,modelPointsC0p05,modelPointsC0p1],lumi,rootFile,plotsOutputDir)
#  PlotAllEfficiencies([modelPointsC0p01,modelPointsC0p05,modelPointsC0p1],lumi,rootFile,plotsOutputDir)
elif sys.argv[1]=='limits':
  print 'limits: DoLimitsAllPoints'
  print 'Warning: will overwrite file',limitsPlotFileName,'if it already exists.'
  if not os.path.isdir(limitsOutputDir):
    os.mkdir(limitsOutputDir)
  with open(limitsOutputDir+'/config.txt', 'w') as file:
    file.write(configString)
  rootFile = TFile(limitsPlotFileName,'recreate')
  DoLimitsAllPoints(cl95MacroPath+cl95MacroName,DoBatch,QueueName,lumi,lumiErr,limitsFileName,limitsOutputDir)
  if not DoBatch: # do mergeLimits automatically if locally running
    print '(auto) mergeLimits: DoMergeCheckAllPoints, DoPlotsAllPoints, DoTablesAllPoints'
    print 'Warning: will overwrite files',limitsFileName+'0p01.txt',limitsFileName+'0p05.txt',limitsFileName+'0p1.txt','if they already exist.'
    DoMergeCheckAllPoints(limitsOutputDir,limitsFileName)
    DoPlotsAllPoints(lumi,rootFile,pathToTDRStyle)
    DoTablesAllPoints(lumi,limitsOutputDir)
elif sys.argv[1]=='mergeLimits':
  print 'mergeLimits: DoMergeCheckAllPoints, DoPlotsAllPoints, DoTablesAllPoints'
  print 'Warning: will overwrite files',limitsFileName+'0p01.txt',limitsFileName+'0p05.txt',limitsFileName+'0p1.txt','if they already exist.'
  rootFile = TFile(limitsPlotFileName,'update')
  DoMergeCheckAllPoints(limitsOutputDir,limitsFileName)
  DoPlotsAllPoints(lumi,rootFile,pathToTDRStyle)
  DoTablesAllPoints(lumi,limitsOutputDir)
elif sys.argv[1]=='plots':
  print 'plots: DoPlotsAllPoints'
  if not os.path.isdir(plotsOutputDir):
    os.mkdir(plotsOutputDir)
  rootFile = TFile(limitsPlotFileName,'update')
  DoPlotsAllPoints(lumi,rootFile,pathToTDRStyle)
elif sys.argv[1]=='tables':
  print 'tables: DoTablesAllPoints'
  rootFile = TFile(limitsPlotFileName)
  DoTablesAllPoints(lumi,limitsOutputDir)
else:
  print 'Did not understand input.'
  Usage()
  sys.exit()

rootFile.Close()


