import FWCore.ParameterSet.Config as cms

process = cms.Process("ExoDiPhotonWithGenAnalysis")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
###'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_100_1_FQI.root'

##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_100_1_FQI.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_101_1_h0P.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_102_1_YEJ.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_103_1_hmj.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_104_1_bme.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_105_1_vpN.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_106_1_9Lh.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_107_1_zQn.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_108_1_et2.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_109_1_bU8.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_10_1_t1d.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_110_1_Vlk.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_111_5_Cue.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_112_1_jn4.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_113_1_nwU.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_114_1_r9o.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_115_1_cPa.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_116_1_7z0.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_117_1_Dwz.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_118_1_JBM.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_11_1_gmE.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_12_1_5S1.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_13_1_S5m.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_14_1_wIi.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_15_1_jHi.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_16_1_Fqc.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_17_1_TRQ.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_18_1_KnU.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_19_1_BFe.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_1_1_j2E.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_20_1_Ih6.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_21_1_ZHA.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_22_1_Kh4.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_23_1_1uS.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_24_1_20C.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_25_1_4iN.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_26_1_r1M.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_27_1_kMu.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_28_1_iUg.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_29_1_LlS.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_2_1_Y7a.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_30_1_IdQ.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_31_1_3vZ.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_32_1_k2u.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_33_1_Vya.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_34_1_dhT.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_35_1_q7w.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_36_1_8ZZ.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_37_1_s7Q.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_38_1_Tdp.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_39_1_Tpc.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_3_1_aTE.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_40_1_ahf.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_41_1_sK4.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_42_1_9L2.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_43_1_g9H.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_44_1_8pX.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_45_1_C0j.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_46_1_UJN.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_47_1_1ig.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_48_1_IkQ.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_49_5_wRA.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_4_1_FtA.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_50_1_OUH.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_51_1_Hu7.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_52_1_D0a.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_53_1_SEf.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_54_1_usk.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_55_1_lJG.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_56_1_nJk.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_57_1_h49.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_58_1_P1j.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_59_1_QId.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_5_1_lak.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_60_1_1nF.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_61_1_vwP.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_62_1_fKO.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_63_1_r09.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_64_1_CdB.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_65_1_peE.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_66_1_vP9.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_67_1_exM.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_68_5_231.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_69_1_HEO.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_6_1_j6I.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_70_1_EW8.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_71_1_qkL.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_72_1_wSq.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_73_1_lQb.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_74_1_j0C.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_75_1_4kr.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_76_1_Iiu.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_77_1_zbs.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_78_1_T69.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_79_1_lH2.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_7_1_hYg.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_80_1_3Me.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_81_1_F0r.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_82_1_6pN.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_83_1_2LV.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_84_1_m4p.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_85_1_bfQ.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_86_1_LaO.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_87_1_ZLD.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_88_1_P32.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_89_1_qiz.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_8_1_gIS.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_90_1_GYZ.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_91_1_O9n.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_92_1_Ttt.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_93_1_qPP.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_94_1_RCj.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_95_1_j0b.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_96_1_NSV.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_97_5_DPI.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_98_1_sD0.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_99_1_SLD.root',
##'root://eoscms//eos/cms/store/user/charaf/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1/EXOMCRECO_Summer12_DR53X_PU_S10_START53_V7C-v1/f556205f5a957fa0f5378b0bc6c8adcb/sherpa_8TeV_gamgam_0j3incl_loop_500mgg1000_BarrelBarrel-v1_Summer12_DR53X_PU_S10_START53_V7C-v1_9_1_VxZ.root'

'file:/afs/cern.ch/work/c/charaf/D2425675-566F-E411-9866-0025905B85B2.root'

     )
)

# need to introduce the global tag now
# because the L1GtUtils method needs to fetch records...
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')

#use the right global tag!
process.GlobalTag.globaltag = 'START53_V7C::All'

# geometry for ecal 
#When in 5_3_X Need to use diff GeometryDB
##process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.GeometryDB_cff")

# file for all histograms for all modules
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('ExoDiPhotonWithGenAnalyzer.root')
)

# filter on good vertex
# based on example in CMSSW/HeavyFlavorAnalysis/Onia2MuMu/test/onia2MuMuPATData_cfg.py
process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
                                           vertexCollection = cms.InputTag('offlinePrimaryVertices'),
                                           minimumNDOF = cms.uint32(4),
                                           maxAbsZ = cms.double(24),	
                                           maxd0 = cms.double(2)	
)
#process.primaryVertexPath = cms.Path(process.primaryVertexFilter)

# filter out scraping
# based on Onia example, and CMSSW/DPGAnalysis/Skims/python/MinBiasPDSkim_cfg.py for the GOODCOLL skim defn
# this requires that if there is >10 tracks,
# then at least 0.25 fraction of them must be 'high purity'

process.noScraping = cms.EDFilter("FilterOutScraping",
                                  applyfilter = cms.untracked.bool(True),
                                  debugOn = cms.untracked.bool(False),
                                  numtrack = cms.untracked.uint32(10),
                                  thresh = cms.untracked.double(0.25)
)

process.load('RecoJets.Configuration.RecoPFJets_cff')
process.kt6PFJets25 = process.kt6PFJets.clone( doRhoFastjet = True )
process.kt6PFJets25.Rho_EtaMax = cms.double(2.5)

#load diphotonWithGen analyzer
process.load("DiPhotonAnalysis.ExoDiPhotonWithGenAnalyzer.exodiphotonwithgenanalyzer_cfi")
process.diphotonWithGenAnalyzer.rho25Correction = cms.InputTag("kt6PFJets25","rho") 
process.diphotonWithGenAnalyzer.ptMin = 70 # pt cut on all photons
process.diphotonWithGenAnalyzer.removeSpikes = False # ie spikes will be exlcuded from tree
process.diphotonWithGenAnalyzer.requireTightPhotons = False # ie only tight photons will be written 
process.diphotonWithGenAnalyzer.requireGenEventInfo = True
process.diphotonWithGenAnalyzer.isMC = False #MC = True or  Data = False
process.diphotonWithGenAnalyzer.IDMethod = cms.untracked.string("ParticleFlow")
process.diphotonWithGenAnalyzer.PFIDCategory = cms.untracked.string("Loose")

# If running on data the following four entries should not be changed. They are loaded into the analyzer as strings but in the case isMC = False then all the both old_pu_n and pu_n will both be filled with -9999.99

process.diphotonWithGenAnalyzer.PUDataFileName = 'PileupDataAug10thHistogram.root' #DataPileUp
process.diphotonWithGenAnalyzer.PUMCFileName = 'PileUpMC.root'  #"MC PileUP"
process.diphotonWithGenAnalyzer.PUDataHistName = "pileup" #Name of histogram in PUDataFileName Need to be binned to 80
process.diphotonWithGenAnalyzer.PUMCHistName = "pu_n_BeforeCuts" #Name of histogram in PUMCFileName  Need to be binned to 80

process.path  = cms.Path(process.primaryVertexFilter+process.noScraping+process.kt6PFJets25+process.diphotonWithGenAnalyzer)

