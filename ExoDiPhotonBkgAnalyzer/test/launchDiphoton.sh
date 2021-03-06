#!/bin/bash

SAMPLE=$1;

mkdir $SAMPLE;
cp exodiphotonbkganalyzer_for_crab_cfg.py $SAMPLE;

cat > ${SAMPLE}/crab.cfg <<EOF


[CRAB]

jobtype = cmssw
scheduler = glite
use_server = 1
server_name=slc5cern

[CMSSW]

# for DY samples
#datasetpath=/${SAMPLE}/Spring10-START3X_V26-v2/GEN-SIM-RECO
#
# for DYToEE_M-20_7TeV-powheg-pythia6 sample
#datasetpath=/${SAMPLE}/Spring10-START3X_V26-v1/GEN-SIM-RECO
#
# for everything else
datasetpath=/${SAMPLE}/Spring10-START3X_V26_S09-v1/GEN-SIM-RECO

pset=exodiphotonbkganalyzer_for_crab_cfg.py

total_number_of_events=-1
events_per_job = 20000
### number_of_jobs = 10

[USER]
return_data = 1

[GRID]

### for RS gravitons
### and for SM diphotons
#ce_white_list = T2_US_Caltech

ce_black_list = T2_US_MIT, T3_GR_Ioannina

EOF

echo " setting up crab env"
# setup crab environment
source /afs/cern.ch/cms/LCG/LCG-2/UI/cms_ui_env.sh;
eval `scramv1 runtime -sh`;
#source /afs/cern.ch/cms/ccs/wm/scripts/Crab/CRAB_2_6_6/crab.sh;
source /afs/cern.ch/cms/ccs/wm/scripts/Crab/crab.sh;


cd ${SAMPLE}

echo " launching crab jobs"
crab -create;
crab -submit;
crab -status;
cd -;

exit
