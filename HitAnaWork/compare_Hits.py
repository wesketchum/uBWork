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

c_roi_peak = TCanvas("c_roi_peak","ROI Peak ADC Canvas",1500,600)
c_roi_peak.Divide(3,1)
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

c_comp_peak = TCanvas("c_comp_peak","Peak Comparison Canvas",1500,600)
c_comp_peak.Divide(3,1)
c_comp_peak.cd(1)
hcomp_peak_0.Draw()
c_comp_peak.cd(2)
hcomp_peak_1.Draw()
c_comp_peak.cd(3)
hcomp_peak_2.Draw()
c_comp_peak.SaveAs("plots/peak_compare.eps")


finalinput = raw_input("Hit enter to exit.")

outputfile = TFile("output.root","RECREATE")
h_roi_peak_0.Write()
h_roi_peak_1.Write()
h_roi_peak_2.Write()
outputfile.Close()

sys.exit()
