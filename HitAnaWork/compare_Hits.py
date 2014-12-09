from ROOT import *
import sys

file_name = "/Users/wketchum/MicroBooNE_Data/hitana_muons_rff.root"

myfile = TFile(file_name,"READ")
mydir  = myfile.Get("hitana")
tree  = mydir.Get("wireDataTree")

#tree.Print()

nbins=200
lowbin=-10
highbin=90

h_roi_peak_0 = TH1F("h_roi_peak_0","ROI Peak ADC, Plane 0;Peak ADC;ROIs",nbins,lowbin,highbin)
h_roi_peak_1 = TH1F("h_roi_peak_1","ROI Peak ADC, Plane 1;Peak ADC;ROIs",nbins,lowbin,highbin)
h_roi_peak_2 = TH1F("h_roi_peak_2","ROI Peak ADC, Plane 2;Peak ADC;ROIs",nbins,lowbin,highbin)

tree.Project("h_roi_peak_0","roi_peak_charge","plane==0")
tree.Project("h_roi_peak_1","roi_peak_charge","plane==1")
tree.Project("h_roi_peak_2","roi_peak_charge","plane==2")

c_roi_peak = TCanvas("c_roi_peak","ROI Peak ADC Canvas",1000,1000)
c_roi_peak.Divide(2,2)
c_roi_peak.cd(1)
h_roi_peak_0.Draw()
c_roi_peak.cd(2)
h_roi_peak_1.Draw()
c_roi_peak.cd(3)
h_roi_peak_2.Draw()
c_roi_peak.SaveAs("plots/roi_peak.eps")

nbins=200
lowbin=-1
highbin=1.5

hcomp_peak_0 = TH1F("hcomp_peak_0","Peak Comparison, Plane 0;(Peak ADC - Peak MC Charge)/MC Charge;ROIs",nbins,lowbin,highbin)
hcomp_peak_1 = TH1F("hcomp_peak_1","Peak Comparison, Plane 1;(Peak ADC - Peak MC Charge)/MC Charge;ROIs",nbins,lowbin,highbin)
hcomp_peak_2 = TH1F("hcomp_peak_2","Peak Comparison, Plane 2;(Peak ADC - Peak MC Charge)/MC Charge;ROIs",nbins,lowbin,highbin)

tree.Project("hcomp_peak_0","(roi_peak_charge-MCHits_PeakCharge)/MCHits_PeakCharge","plane==0")
tree.Project("hcomp_peak_1","(roi_peak_charge-MCHits_PeakCharge)/MCHits_PeakCharge","plane==1")
tree.Project("hcomp_peak_2","(roi_peak_charge-MCHits_PeakCharge)/MCHits_PeakCharge","plane==2")

c_comp_peak = TCanvas("c_comp_peak","Peak Comparison Canvas",1000,1000)
c_comp_peak.Divide(2,2)
c_comp_peak.cd(1)
hcomp_peak_0.Draw()
c_comp_peak.cd(2)
hcomp_peak_1.Draw()
c_comp_peak.cd(3)
hcomp_peak_2.Draw()
c_comp_peak.SaveAs("plots/peak_compare.eps")


nbins=20
lowbin=-10
highbin=10

hcomp_peaktime_0 = TH1F("hcomp_peaktime_0","Peak Time Comparison, Plane 0;Peak ROI Time - Peak MC Time;ROIs",nbins,lowbin,highbin)
hcomp_peaktime_1 = TH1F("hcomp_peaktime_1","Peak Time Comparison, Plane 1;Peak ROI Time - Peak MC Time;ROIs",nbins,lowbin,highbin)
hcomp_peaktime_2 = TH1F("hcomp_peaktime_2","Peak Time Comparison, Plane 2;Peak ROI Time - Peak MC Time;ROIs",nbins,lowbin,highbin)

tree.Project("hcomp_peaktime_0","(roi_peak_time-MCHits_Peak)","plane==0")
tree.Project("hcomp_peaktime_1","(roi_peak_time-MCHits_Peak)","plane==1")
tree.Project("hcomp_peaktime_2","(roi_peak_time-MCHits_Peak)","plane==2")

c_comp_peaktime = TCanvas("c_comp_peaktime","Peak Time Comparison Canvas",1000,1000)
c_comp_peaktime.Divide(2,2)
c_comp_peaktime.cd(1)
hcomp_peaktime_0.Draw()
c_comp_peaktime.cd(2)
hcomp_peaktime_1.Draw()
c_comp_peaktime.cd(3)
hcomp_peaktime_2.Draw()
c_comp_peaktime.SaveAs("plots/peaktime_compare.eps")

nbins=200
lowbin=-10
highbin=90

h_g_peak_0 = TH1F("h_g_peak_0","GaussHit Peak ADC, Plane 0;Peak ADC;ROIs",nbins,lowbin,highbin)
h_g_peak_1 = TH1F("h_g_peak_1","GaussHit Peak ADC, Plane 1;Peak ADC;ROIs",nbins,lowbin,highbin)
h_g_peak_2 = TH1F("h_g_peak_2","GaussHit Peak ADC, Plane 2;Peak ADC;ROIs",nbins,lowbin,highbin)
h_cc_peak_0 = TH1F("h_cc_peak_0","CCHit Peak ADC, Plane 0;Peak ADC;ROIs",nbins,lowbin,highbin)
h_cc_peak_1 = TH1F("h_cc_peak_1","CCHit Peak ADC, Plane 1;Peak ADC;ROIs",nbins,lowbin,highbin)
h_cc_peak_2 = TH1F("h_cc_peak_2","CCHit Peak ADC, Plane 2;Peak ADC;ROIs",nbins,lowbin,highbin)
h_rff_peak_0 = TH1F("h_rff_peak_0","RFFHit Peak ADC, Plane 0;Peak ADC;ROIs",nbins,lowbin,highbin)
h_rff_peak_1 = TH1F("h_rff_peak_1","RFFHit Peak ADC, Plane 1;Peak ADC;ROIs",nbins,lowbin,highbin)
h_rff_peak_2 = TH1F("h_rff_peak_2","RFFHit Peak ADC, Plane 2;Peak ADC;ROIs",nbins,lowbin,highbin)

tree.Project("h_g_peak_0","Hits_PeakCharge[0]","plane==0")
tree.Project("h_g_peak_1","Hits_PeakCharge[0]","plane==1")
tree.Project("h_g_peak_2","Hits_PeakCharge[0]","plane==2")
tree.Project("h_cc_peak_0","Hits_PeakCharge[1]","plane==0")
tree.Project("h_cc_peak_1","Hits_PeakCharge[1]","plane==1")
tree.Project("h_cc_peak_2","Hits_PeakCharge[1]","plane==2")
tree.Project("h_rff_peak_0","Hits_PeakCharge[2]","plane==0")
tree.Project("h_rff_peak_1","Hits_PeakCharge[2]","plane==1")
tree.Project("h_rff_peak_2","Hits_PeakCharge[2]","plane==2")

nbins=200
lowbin=-0.05
highbin=0.1

hcomp_g_peak_0 = TH1F("hcomp_g_peak_0","Peak Comparison, Plane 0;(Hit peak ADC - ROI peak ADC)/ROI peak ADC;ROIs",nbins,lowbin,highbin)
hcomp_g_peak_1 = TH1F("hcomp_g_peak_1","Peak Comparison, Plane 1;(Hit peak ADC - ROI peak ADC)/ROI peak ADC;ROIs",nbins,lowbin,highbin)
hcomp_g_peak_2 = TH1F("hcomp_g_peak_2","Peak Comparison, Plane 2;(Hit peak ADC - ROI peak ADC)/ROI peak ADC;ROIs",nbins,lowbin,highbin)
tree.Project("hcomp_g_peak_0","(Hits_PeakCharge[0]-roi_peak_charge)/roi_peak_charge","plane==0 && roi_peak_charge>1 && NHits[0]>0")
tree.Project("hcomp_g_peak_1","(Hits_PeakCharge[0]-roi_peak_charge)/roi_peak_charge","plane==1 && roi_peak_charge>1 && NHits[0]>0")
tree.Project("hcomp_g_peak_2","(Hits_PeakCharge[0]-roi_peak_charge)/roi_peak_charge","plane==2 && roi_peak_charge>1 && NHits[0]>0")
hcomp_g_peak_0.SetLineColor(kBlack)
hcomp_g_peak_0.SetLineWidth(2)
hcomp_g_peak_1.SetLineColor(kBlack)
hcomp_g_peak_1.SetLineWidth(2)
hcomp_g_peak_2.SetLineColor(kBlack)
hcomp_g_peak_2.SetLineWidth(2)


hcomp_cc_peak_0 = TH1F("hcomp_cc_peak_0","Peak Comparison, Plane 0;(Hit peak ADC - ROI peak ADC)/ROI peak ADC;ROIs",nbins,lowbin,highbin)
hcomp_cc_peak_1 = TH1F("hcomp_cc_peak_1","Peak Comparison, Plane 1;(Hit peak ADC - ROI peak ADC)/ROI peak ADC;ROIs",nbins,lowbin,highbin)
hcomp_cc_peak_2 = TH1F("hcomp_cc_peak_2","Peak Comparison, Plane 2;(Hit peak ADC - ROI peak ADC)/ROI peak ADC;ROIs",nbins,lowbin,highbin)
tree.Project("hcomp_cc_peak_0","(Hits_PeakCharge[1]-roi_peak_charge)/roi_peak_charge","plane==0 && roi_peak_charge>1 && NHits[1]>0")
tree.Project("hcomp_cc_peak_1","(Hits_PeakCharge[1]-roi_peak_charge)/roi_peak_charge","plane==1 && roi_peak_charge>1 && NHits[1]>0")
tree.Project("hcomp_cc_peak_2","(Hits_PeakCharge[1]-roi_peak_charge)/roi_peak_charge","plane==2 && roi_peak_charge>1 && NHits[1]>0")
hcomp_cc_peak_0.SetLineColor(kRed)
hcomp_cc_peak_0.SetLineWidth(2)
hcomp_cc_peak_1.SetLineColor(kRed)
hcomp_cc_peak_1.SetLineWidth(2)
hcomp_cc_peak_2.SetLineColor(kRed)
hcomp_cc_peak_2.SetLineWidth(2)

hcomp_rff_peak_0 = TH1F("hcomp_rff_peak_0","Peak Comparison, Plane 0;(Hit peak ADC - ROI peak ADC)/ROI peak ADC;ROIs",nbins,lowbin,highbin)
hcomp_rff_peak_1 = TH1F("hcomp_rff_peak_1","Peak Comparison, Plane 1;(Hit peak ADC - ROI peak ADC)/ROI peak ADC;ROIs",nbins,lowbin,highbin)
hcomp_rff_peak_2 = TH1F("hcomp_rff_peak_2","Peak Comparison, Plane 2;(Hit peak ADC - ROI peak ADC)/ROI peak ADC;ROIs",nbins,lowbin,highbin)
tree.Project("hcomp_rff_peak_0","(Hits_PeakCharge[2]-roi_peak_charge)/roi_peak_charge","plane==0 && roi_peak_charge>1 && NHits[2]>0")
tree.Project("hcomp_rff_peak_1","(Hits_PeakCharge[2]-roi_peak_charge)/roi_peak_charge","plane==1 && roi_peak_charge>1 && NHits[2]>0")
tree.Project("hcomp_rff_peak_2","(Hits_PeakCharge[2]-roi_peak_charge)/roi_peak_charge","plane==2 && roi_peak_charge>1 && NHits[2]>0")
hcomp_rff_peak_0.SetLineColor(kBlue)
hcomp_rff_peak_0.SetLineWidth(2)
hcomp_rff_peak_1.SetLineColor(kBlue)
hcomp_rff_peak_1.SetLineWidth(2)
hcomp_rff_peak_2.SetLineColor(kBlue)
hcomp_rff_peak_2.SetLineWidth(2)

c_comp_hits_peak = TCanvas("c_comp_hits_peak","Reconstructed Peak Amplitude Comparison Canvas",1000,1000)
c_comp_hits_peak.Divide(2,2)
c_comp_hits_peak.cd(1)
hcomp_rff_peak_0.Draw()
hcomp_cc_peak_0.Draw("same")
hcomp_g_peak_0.Draw("same")
c_comp_hits_peak.cd(2)
hcomp_rff_peak_1.Draw()
hcomp_cc_peak_1.Draw("same")
hcomp_g_peak_1.Draw("same")
c_comp_hits_peak.cd(3)
hcomp_rff_peak_2.Draw()
hcomp_cc_peak_2.Draw("same")
hcomp_g_peak_2.Draw("same")
c_comp_hits_peak.cd(4)
legend = TLegend(0.1,0.1,0.9,0.9)
legend.AddEntry(hcomp_g_peak_0,"GaussHit","l")
legend.AddEntry(hcomp_cc_peak_0,"CCHit","l")
legend.AddEntry(hcomp_rff_peak_0,"RFFHit","l")
legend.Draw()
c_comp_hits_peak.SaveAs("plots/hits_peak_compare.eps")

c_comp_hits_peak.cd(1)
hcomp_cc_peak_0.Draw()
hcomp_g_peak_0.Draw("same")
c_comp_hits_peak.cd(2)
hcomp_cc_peak_1.Draw()
hcomp_g_peak_1.Draw("same")
c_comp_hits_peak.cd(3)
hcomp_cc_peak_2.Draw()
hcomp_g_peak_2.Draw("same")
c_comp_hits_peak.cd(4)
legend = TLegend(0.1,0.1,0.9,0.9)
legend.AddEntry(hcomp_g_peak_0,"GaussHit","l")
legend.AddEntry(hcomp_cc_peak_0,"CCHit","l")
legend.Draw()
c_comp_hits_peak.SaveAs("plots/hits_peak_compare_norff.eps")


nbins=100
lowbin=-2
highbin=2

hcomp_g_peaktime_0 = TH1F("hcomp_g_peaktime_0","Peak time comparison, Plane 0;(Hit peak tick - ROI peak tick);ROIs",nbins,lowbin,highbin)
hcomp_g_peaktime_1 = TH1F("hcomp_g_peaktime_1","Peak time comparison, Plane 1;(Hit peak tick - ROI peak tick);ROIs",nbins,lowbin,highbin)
hcomp_g_peaktime_2 = TH1F("hcomp_g_peaktime_2","Peak time comparison, Plane 2;(Hit peak tick - ROI peak tick);ROIs",nbins,lowbin,highbin)
tree.Project("hcomp_g_peaktime_0","(Hits_Peak[0]-roi_peak_time)","plane==0 && roi_peak_charge>1 && NHits[0]>0")
tree.Project("hcomp_g_peaktime_1","(Hits_Peak[0]-roi_peak_time)","plane==1 && roi_peak_charge>1 && NHits[0]>0")
tree.Project("hcomp_g_peaktime_2","(Hits_Peak[0]-roi_peak_time)","plane==2 && roi_peak_charge>1 && NHits[0]>0")
hcomp_g_peaktime_0.SetLineColor(kBlack)
hcomp_g_peaktime_0.SetLineWidth(2)
hcomp_g_peaktime_1.SetLineColor(kBlack)
hcomp_g_peaktime_1.SetLineWidth(2)
hcomp_g_peaktime_2.SetLineColor(kBlack)
hcomp_g_peaktime_2.SetLineWidth(2)


hcomp_cc_peaktime_0 = TH1F("hcomp_cc_peaktime_0","Peak time comparison, Plane 0;(Hit peak tick - ROI peak tick);ROIs",nbins,lowbin,highbin)
hcomp_cc_peaktime_1 = TH1F("hcomp_cc_peaktime_1","Peak time comparison, Plane 1;(Hit peak tick - ROI peak tick);ROIs",nbins,lowbin,highbin)
hcomp_cc_peaktime_2 = TH1F("hcomp_cc_peaktime_2","Peak time comparison, Plane 2;(Hit peak tick - ROI peak tick);ROIs",nbins,lowbin,highbin)
tree.Project("hcomp_cc_peaktime_0","(Hits_Peak[1]-roi_peak_time)","plane==0 && roi_peak_charge>1 && NHits[1]>0")
tree.Project("hcomp_cc_peaktime_1","(Hits_Peak[1]-roi_peak_time)","plane==1 && roi_peak_charge>1 && NHits[1]>0")
tree.Project("hcomp_cc_peaktime_2","(Hits_Peak[1]-roi_peak_time)","plane==2 && roi_peak_charge>1 && NHits[1]>0")
hcomp_cc_peaktime_0.SetLineColor(kRed)
hcomp_cc_peaktime_0.SetLineWidth(2)
hcomp_cc_peaktime_1.SetLineColor(kRed)
hcomp_cc_peaktime_1.SetLineWidth(2)
hcomp_cc_peaktime_2.SetLineColor(kRed)
hcomp_cc_peaktime_2.SetLineWidth(2)

hcomp_rff_peaktime_0 = TH1F("hcomp_rff_peaktime_0","Peak time comparison, Plane 0;(Hit peak tick - ROI peak tick);ROIs",nbins,lowbin,highbin)
hcomp_rff_peaktime_1 = TH1F("hcomp_rff_peaktime_1","Peak time comparison, Plane 1;(Hit peak tick - ROI peak tick);ROIs",nbins,lowbin,highbin)
hcomp_rff_peaktime_2 = TH1F("hcomp_rff_peaktime_2","Peak time comparison, Plane 2;(Hit peak tick - ROI peak tick);ROIs",nbins,lowbin,highbin)
tree.Project("hcomp_rff_peaktime_0","(Hits_Peak[2]-roi_peak_time)","plane==0 && roi_peak_charge>1 && NHits[2]>0")
tree.Project("hcomp_rff_peaktime_1","(Hits_Peak[2]-roi_peak_time)","plane==1 && roi_peak_charge>1 && NHits[2]>0")
tree.Project("hcomp_rff_peaktime_2","(Hits_Peak[2]-roi_peak_time)","plane==2 && roi_peak_charge>1 && NHits[2]>0")
hcomp_rff_peaktime_0.SetLineColor(kBlue)
hcomp_rff_peaktime_0.SetLineWidth(2)
hcomp_rff_peaktime_1.SetLineColor(kBlue)
hcomp_rff_peaktime_1.SetLineWidth(2)
hcomp_rff_peaktime_2.SetLineColor(kBlue)
hcomp_rff_peaktime_2.SetLineWidth(2)

c_comp_hits_peaktime = TCanvas("c_comp_hits_peaktime","Reconstructed Peak Amplitude Comparison Canvas",1000,1000)
c_comp_hits_peaktime.Divide(2,2)
c_comp_hits_peaktime.cd(1)
hcomp_rff_peaktime_0.Draw()
hcomp_cc_peaktime_0.Draw("same")
hcomp_g_peaktime_0.Draw("same")
c_comp_hits_peaktime.cd(2)
hcomp_rff_peaktime_1.Draw()
hcomp_cc_peaktime_1.Draw("same")
hcomp_g_peaktime_1.Draw("same")
c_comp_hits_peaktime.cd(3)
hcomp_rff_peaktime_2.Draw()
hcomp_cc_peaktime_2.Draw("same")
hcomp_g_peaktime_2.Draw("same")
c_comp_hits_peaktime.cd(4)
legend = TLegend(0.1,0.1,0.9,0.9)
legend.AddEntry(hcomp_g_peaktime_0,"GaussHit","l")
legend.AddEntry(hcomp_cc_peaktime_0,"CCHit","l")
legend.AddEntry(hcomp_rff_peaktime_0,"RFFHit","l")
legend.Draw()
c_comp_hits_peaktime.SaveAs("plots/hits_peaktime_compare.eps")

finalinput = raw_input("Hit enter to exit.")

sys.exit()
