#!/usr/bin/env python

import subprocess

from ROOT import *

# Make comparison between limits with and without deltaPhi cut
#
# Seth Cooper, U. Alabama


deltaPhiCutResultDir = 'oct16_5pctPtSystTest_1p5pctScaleShifts_symmWindowSSBOpt_loosePFIDJun12_local_limits'
noDeltaPhiCutResultDir = 'sep29_1p5pctScaleShifts_symmWindowSSBOpt_loosePFIDJun12_local_limits'

deltaPhiCutRootFileName = deltaPhiCutResultDir+'/plots.root'
noDeltaPhiCutRootFileName = noDeltaPhiCutResultDir+'/plots.root'

tfileNoCut = TFile.Open(noDeltaPhiCutRootFileName)
tfileDPhiCut = TFile.Open(deltaPhiCutRootFileName)

limitsExpNoCutk0p01 = tfileNoCut.Get('limitExpGraph_k0.01')
limitsExpNoCutk0p01.SetLineStyle(2)
limitsExpNoCutk0p01.SetLineWidth(2)
limitsExpNoCutk0p01.SetName('limitExpGraph0p01NoCut')
limitsExpNoCutk0p05 = tfileNoCut.Get('limitExpGraph_k0.05')
limitsExpNoCutk0p05.SetLineStyle(2)
limitsExpNoCutk0p05.SetLineWidth(2)
limitsExpNoCutk0p01.SetName('limitExpGraph0p05NoCut')
limitsExpNoCutk0p1 = tfileNoCut.Get('limitExpGraph_k0.1')
limitsExpNoCutk0p1.SetLineStyle(2)
limitsExpNoCutk0p1.SetLineWidth(2)
limitsExpNoCutk0p01.SetName('limitExpGraph0p1NoCut')
#
limitsExpDPhiCutk0p01 = tfileDPhiCut.Get('limitExpGraph_k0.01')
limitsExpDPhiCutk0p01.SetLineStyle(1)
limitsExpDPhiCutk0p01.SetLineWidth(1)
limitsExpDPhiCutk0p05 = tfileDPhiCut.Get('limitExpGraph_k0.05')
limitsExpDPhiCutk0p05.SetLineStyle(1)
limitsExpDPhiCutk0p05.SetLineWidth(1)
limitsExpDPhiCutk0p1 = tfileDPhiCut.Get('limitExpGraph_k0.1')
limitsExpDPhiCutk0p1.SetLineStyle(1)
limitsExpDPhiCutk0p1.SetLineWidth(1)
#
limitsExpNoCutk0p01.SetMarkerColor(2)
limitsExpNoCutk0p01.SetMarkerStyle(22)
limitsExpNoCutk0p01.SetMarkerSize(1.5)
limitsExpNoCutk0p05.SetMarkerColor(4)
limitsExpNoCutk0p05.SetMarkerStyle(22)
limitsExpNoCutk0p05.SetMarkerSize(1.5)
limitsExpNoCutk0p1.SetMarkerColor(8)
limitsExpNoCutk0p1.SetMarkerStyle(22)
limitsExpNoCutk0p1.SetMarkerSize(1.5)
limitsExpDPhiCutk0p01.SetMarkerColor(2)
limitsExpDPhiCutk0p01.SetMarkerStyle(20)
limitsExpDPhiCutk0p01.SetMarkerSize(1.1)
limitsExpDPhiCutk0p05.SetMarkerColor(4)
limitsExpDPhiCutk0p05.SetMarkerStyle(20)
limitsExpDPhiCutk0p05.SetMarkerSize(1.1)
limitsExpDPhiCutk0p1.SetMarkerColor(8)
limitsExpDPhiCutk0p1.SetMarkerStyle(20)
limitsExpDPhiCutk0p1.SetMarkerSize(1.1)
#
thGraph0p01 = tfileNoCut.Get('thGraph_k0.01')
thGraph0p01.SetLineStyle(7)
thGraph0p01.SetLineColor(2)
thGraph0p05 = tfileNoCut.Get('thGraph_k0.05')
thGraph0p05.SetLineStyle(7)
thGraph0p05.SetLineColor(4)
thGraph0p1 = tfileNoCut.Get('thGraph_k0.1')
thGraph0p1.SetLineStyle(7)
thGraph0p1.SetLineColor(8)
#
c = TCanvas("c", "c",0,0,600,600)
gStyle.SetOptFit(1)
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
c.SetHighLightColor(2)
c.Range(200,-3.536669,3637.5,-2.469521)
c.SetFillColor(0)
c.SetBorderMode(0)
c.SetBorderSize(2)
c.SetLogy()
c.SetTickx(1)
c.SetTicky(1)
c.SetLeftMargin(0.18)
c.SetRightMargin(0.04)
c.SetTopMargin(0.05)
c.SetBottomMargin(0.15)
c.SetFrameFillStyle(0)
c.SetFrameLineWidth(2)
c.SetFrameBorderMode(0)
c.SetFrameFillStyle(0)
c.SetFrameLineWidth(2)
c.SetFrameBorderMode(0)

test = TH1F("test","test",10,750,3500)
test.SetMinimum(0.0002)
test.SetMaximum(0.003)
test.SetStats(0)
#test.SetLineStyle(0)
#test.SetLineWidth(2)
#test.SetMarkerStyle(20)
#test.SetMarkerSize(0.8)
test.GetXaxis().SetTitle("M_{1} [GeV]")
test.GetXaxis().SetLabelFont(42)
test.GetXaxis().SetLabelOffset(0.007)
test.GetXaxis().SetTitleOffset(1.2)
test.GetXaxis().SetTitleFont(42)
test.GetYaxis().SetTitle("RS graviton #sigma [pb]     ")
test.GetYaxis().SetLabelFont(42)
test.GetYaxis().SetLabelOffset(0.007)
test.GetYaxis().SetTitleOffset(1.5)
test.GetYaxis().SetTitleFont(42)
test.GetZaxis().SetLabelFont(42)
test.GetZaxis().SetLabelOffset(0.007)
test.GetZaxis().SetLabelSize(0.05)
test.GetZaxis().SetTitleSize(0.06)
test.GetZaxis().SetTitleOffset(1.1)
test.GetZaxis().SetTitleFont(42)
test.Draw()

mg = TMultiGraph()
mg.Add(limitsExpNoCutk0p01,"lp")
mg.Add(limitsExpNoCutk0p05,"lp")
mg.Add(limitsExpNoCutk0p1,"lp")
mg.Add(limitsExpDPhiCutk0p01,"lp")
mg.Add(limitsExpDPhiCutk0p05,"lp")
mg.Add(limitsExpDPhiCutk0p1,"lp")
#
mg.Add(thGraph0p01,"l")
mg.Add(thGraph0p05,"l")
mg.Add(thGraph0p1,"l")
mg.Draw("l")

leg = TLegend(0.42,0.71,0.73,0.92)
leg.SetBorderSize(0)
leg.SetLineColor(1)
leg.SetLineStyle(1)
leg.SetLineWidth(2)
leg.SetFillColor(0)
leg.SetFillStyle(0)
entry=leg.AddEntry(limitsExpNoCutk0p01,"95% CL limit (3% Pt scale syst ) #tilde{k} = 0.01","LP")
#entry.SetLineColor(2)
#entry.SetLineStyle(2)
#entry.SetLineWidth(4)
#entry.SetMarkerColor(2)
#entry.SetMarkerStyle(22)
#entry.SetMarkerSize(1)
entry=leg.AddEntry(limitsExpNoCutk0p05,"95% CL limit (3% Pt scale syst) #tilde{k} = 0.05","LP")
#entry.SetLineColor(4)
#entry.SetLineStyle(2)
#entry.SetLineWidth(4)
#entry.SetMarkerColor(4)
#entry.SetMarkerStyle(22)
#entry.SetMarkerSize(1)
entry=leg.AddEntry(limitsExpNoCutk0p1,"95% CL limit (3% Pt scale syst) #tilde{k} = 0.1","LP")
#entry.SetLineColor(8)
#entry.SetLineStyle(2)
#entry.SetLineWidth(4)
#entry.SetMarkerColor(8)
#entry.SetMarkerStyle(22)
#entry.SetMarkerSize(1)
#
entry=leg.AddEntry(limitsExpDPhiCutk0p01,"95% CL limit (5% Pt scale syst) #tilde{k} = 0.01","LP")
#entry.SetLineColor(2)
#entry.SetLineStyle(1)
#entry.SetLineWidth(4)
#entry.SetMarkerColor(2)
#entry.SetMarkerStyle(24)
#entry.SetMarkerSize(1)
entry=leg.AddEntry(limitsExpDPhiCutk0p05,"95% CL limit (5% Pt scale syst) #tilde{k} = 0.05","LP")
#entry.SetLineColor(4)
#entry.SetLineStyle(1)
#entry.SetLineWidth(4)
#entry.SetMarkerColor(4)
#entry.SetMarkerStyle(24)
#entry.SetMarkerSize(1)
entry=leg.AddEntry(limitsExpDPhiCutk0p1,"95% CL limit (5% Pt scale syst) #tilde{k} = 0.1","LP")
#entry.SetLineColor(8)
#entry.SetLineStyle(1)
#entry.SetLineWidth(4)
#entry.SetMarkerColor(8)
#entry.SetMarkerStyle(24)
#entry.SetMarkerSize(1)
leg.Draw()

#pt = TPaveText(0.645973,0.629371,0.845638,0.699301,"blNDC")
#pt.SetName("CMS Preliminary")
#pt.SetBorderSize(1)
#pt.SetFillColor(0)
#pt.SetFillStyle(0)
#pt.SetLineColor(0)
#pt.SetLineWidth(2)
#pt.SetTextFont(42)
#pt.SetTextSize(0.0354545)
#text = pt.AddText("CMS Preliminary")
#pt.Draw()
#
#pt = TPaveText(0.654362,0.585664,0.825503,0.652098,"blNDC")
#pt.SetBorderSize(1)
#pt.SetFillColor(0)
#pt.SetFillStyle(0)
#pt.SetLineColor(0)
#pt.SetLineWidth(2)
#pt.SetTextFont(42)
#pt.SetTextSize(0.0354545)
#text = pt.AddText("10.3 fb^{-1} at 8 TeV")
#pt.Draw()

test__6 = TH1F("test__6","test",10,750,3500)
test__6.SetMinimum(0.0002)
test__6.SetMaximum(0.003)
test__6.SetDirectory(0)
test__6.SetStats(0)
#test__6.SetLineStyle(0)
#test__6.SetLineWidth(2)
#test__6.SetMarkerStyle(20)
#test__6.SetMarkerSize(0.8)
test__6.GetXaxis().SetTitle("M_{1} [GeV]")
test__6.GetXaxis().SetLabelFont(42)
test__6.GetXaxis().SetLabelOffset(0.007)
test__6.GetXaxis().SetTitleOffset(1.2)
test__6.GetXaxis().SetTitleFont(42)
test__6.GetYaxis().SetTitle("RS graviton #sigma [pb]     ")
test__6.GetYaxis().SetLabelFont(42)
test__6.GetYaxis().SetLabelOffset(0.007)
test__6.GetYaxis().SetTitleOffset(1.5)
test__6.GetYaxis().SetTitleFont(42)
test__6.GetZaxis().SetLabelFont(42)
test__6.GetZaxis().SetLabelOffset(0.007)
test__6.GetZaxis().SetLabelSize(0.05)
test__6.GetZaxis().SetTitleSize(0.06)
test__6.GetZaxis().SetTitleOffset(1.1)
test__6.GetZaxis().SetTitleFont(42)
test__6.Draw("sameaxis")

#c.Print("allLimitsCompared.pdf")
#subprocess.Popen(['convert','-trim',"allLimitsCompared.pdf","allLimitsCompared.png"])

## wait for input to keep the GUI (which lives on a ROOT event dispatcher) alive
if __name__ == '__main__':
   rep = ''
   while not rep in [ 'q', 'Q' ]:
      rep = raw_input( 'enter "q" to quit: ' )
      if 1 < len(rep):
         rep = rep[0]


