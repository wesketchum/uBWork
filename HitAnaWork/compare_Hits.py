import sys
sys.path.insert(1,"../Utilities")

from ROOT import *
from Root_Functions import *

if len(sys.argv)!=2:
    print "Usage: python compare_Hits.py input_file"
    sys.exit()

file_name = sys.argv[1]
print "Opening file ", file_name

myfile = TFile(file_name,"READ")
mydir  = myfile.Get("hitana")
tree  = mydir.Get("wireDataTree")

def CreateHist(nbins,lowbin,highbin,name,plane,title,xaxis):
    hname = "h_"+name+"_"+str(plane)
    htitle = title+", Plane "+str(plane)+";"+xaxis+";ROIs"
    return TH1F(hname,htitle,nbins,lowbin,highbin)

def CreateHistSet(nbins,lowbin,highbin,name,title,xaxis,tree,val,cuts="1",color=kBlack,linestyle=1):
    hists = []
    for p in range(0,3):
        hists.append(CreateHist(nbins,lowbin,highbin,name,p,title,xaxis))
        tree.Project(hists[-1].GetName(),val,"plane=="+str(p)+"&&"+cuts)
        HistShowOverflow(hists[-1])
        hists[-1].SetLineWidth(2)
        hists[-1].SetLineColor(color)
        hists[-1].SetLineStyle(linestyle)
    return hists

def CreateCanvas(name,title,hists):
    can = TCanvas("c_"+name,title+" Canvas",1000,1000)
    can.Divide(2,2)
    for c in range(0,3):
        can.cd(c+1)
        hists[c].Draw()
    can.SaveAs("plots/"+name+".eps")
    return can

def CreateCanvas2(name,title,labels,hists1,hists2):
    can = TCanvas("c_"+name,title+" Canvas",1000,1000)
    can.Divide(2,2)
    for c in range(0,3):
        can.cd(c+1)
        hists1[c].Draw()
        hists2[c].Draw("same")
    can.cd(4)
    legend = TLegend(0.1,0.1,0.9,0.9)
    legend.AddEntry(hists1[0],labels[0],"l")
    legend.AddEntry(hists2[0],labels[1],"l")
    legend.Draw()
    can.SaveAs("plots/"+name+".eps")
    return can

def CreateCanvas3(name,title,labels,hists1,hists2,hists3):
    can = TCanvas("c_"+name,title+" Canvas",1000,1000)
    can.Divide(2,2)
    for c in range(0,3):
        can.cd(c+1)
        hists1[c].Draw()
        hists2[c].Draw("same")
        hists3[c].Draw("same")
    can.cd(4)
    legend = TLegend(0.1,0.1,0.9,0.9)
    legend.AddEntry(hists1[0],labels[0],"l")
    legend.AddEntry(hists2[0],labels[1],"l")
    legend.AddEntry(hists3[0],labels[2],"l")
    legend.Draw()
    can.SaveAs("plots/"+name+".eps")
    return can


name = "roi_peak"
title = "ROI Peak ADC"
hists_roi_peak = CreateHistSet(125,-10,140,name,title,"ROI peak ADC",tree,"roi_peak_charge")
c_roi_peak = CreateCanvas(name,title,hists_roi_peak)
c_roi_peak.Draw()

name = "roi_integral"
title = "ROI Integral ADC"
hists_roi_integral = CreateHistSet(150,-100,1500,name,title,"ROI integral ADC",tree,"roi_charge")
c_roi_integral = CreateCanvas(name,title,hists_roi_integral)
c_roi_integral.Draw()

h_roi_charge_prof_0 = TProfile("h_roi_charge_prof_0","ROI integral vs. peak, Plane 0;ROI peak charge;ROI integral / ROI size",100,0,50)
h_roi_charge_prof_1 = TProfile("h_roi_charge_prof_1","ROI integral vs. peak, Plane 1;ROI peak charge;ROI integral / ROI size",100,0,50)
h_roi_charge_prof_2 = TProfile("h_roi_charge_prof_2","ROI integral vs. peak, Plane 2;ROI peak charge;ROI integral / ROI size",100,0,50)
tree.Project(h_roi_charge_prof_0.GetName(),"roi_charge/roi_size:roi_peak_charge","plane==0")
tree.Project(h_roi_charge_prof_1.GetName(),"roi_charge/roi_size:roi_peak_charge","plane==1")
tree.Project(h_roi_charge_prof_2.GetName(),"roi_charge/roi_size:roi_peak_charge","plane==2")
h_roi_charge_prof_0.Fit("pol1","","",7,30)
h_roi_charge_prof_1.Fit("pol1","","",7,30)
h_roi_charge_prof_2.Fit("pol1","","",7,30)
h_roi_charge_profs = [ h_roi_charge_prof_0, h_roi_charge_prof_1, h_roi_charge_prof_2 ]
c_roi_charge_prof = CreateCanvas("roi_charge_prof","ROI integral vs peak",h_roi_charge_profs)
c_roi_charge_prof.SaveAs("plots/roi_charge_prof.eps")
c_roi_charge_prof.Draw()

input("Press enter to continue.")

name = "peak_compare"
title = "Peak comparison"
hists_comp_peak = CreateHistSet(125,-1,1.4,
                               name,title,
                               "(ROI peak ADC - Peak MC charge)/Peak MC charge",
                               tree,
                               "(roi_peak_charge-MCHits_PeakCharge)/MCHits_PeakCharge")
c_comp_peak = CreateCanvas(name,title,hists_comp_peak)
c_comp_peak.Draw()


name = "peaktime_compare"
title = "Peak time comparison"
hists_comp_peaktime = CreateHistSet(20,-10,10,
                                    name,title,
                                    "(ROI peak tick - MC peack tick)",
                                    tree,
                                    "(roi_peak_time-MCHits_Peak)")
c_comp_peaktime = CreateCanvas(name,title,hists_comp_peaktime)
c_comp_peaktime.Draw()


nbins=150
lowbin=-0.15
highbin=0.15
name="peak_compare"
title="Hits peak comparison"
xaxis="(Hit peak ADC - ROI peak ADC)/ROI peak ADC"
hists_comp_g_peak = CreateHistSet(nbins,lowbin,highbin,
                                  name+"_g",title,xaxis,
                                  tree,
                                  "(Hits_PeakCharge[0]-roi_peak_charge)/roi_peak_charge",
                                  "roi_peak_charge>1&&NHits[0]>0",
                                  kBlack)
hists_comp_c_peak = CreateHistSet(nbins,lowbin,highbin,
                                  name+"_c",title,xaxis,
                                  tree,
                                  "(Hits_PeakCharge[1]-roi_peak_charge)/roi_peak_charge",
                                  "roi_peak_charge>1&&NHits[1]>0",
                                  kRed)
hists_comp_r_peak = CreateHistSet(nbins,lowbin,highbin,
                                  name+"_r",title,xaxis,
                                  tree,
                                  "(Hits_PeakCharge[2]-roi_peak_charge)/roi_peak_charge",
                                  "roi_peak_charge>1&&NHits[2]>0",
                                  kBlue)
labels = ["RFFHit","CCHit","GaussHit"]
c_comp_hits_peak = CreateCanvas3("hits_peak_compare",title,labels,
                                 hists_comp_r_peak,hists_comp_c_peak,hists_comp_g_peak)
c_comp_hits_peak.Draw()

labels = ["CCHit","GaussHit"]
c_comp_hits_peak_norff = CreateCanvas2("hits_peak_compare_norff",title,labels,
                                       hists_comp_c_peak,hists_comp_g_peak)
c_comp_hits_peak_norff.Draw()


nbins=100
lowbin=-5
highbin=5
name="peaktime_compare"
title="Hits peak tick comparison"
xaxis="(Hit peak tick - ROI peak tick)"
hists_comp_g_peaktime = CreateHistSet(nbins,lowbin,highbin,
                                      name+"_g",title,xaxis,
                                      tree,
                                      "(Hits_Peak[0]-roi_peak_time)",
                                      "roi_peak_charge>1&&NHits[0]>0",
                                      kBlack)
hists_comp_c_peaktime = CreateHistSet(nbins,lowbin,highbin,
                                      name+"_c",title,xaxis,
                                      tree,
                                      "(Hits_Peak[1]-roi_peak_time)",
                                      "roi_peak_charge>1&&NHits[1]>0",
                                      kRed)
hists_comp_r_peaktime = CreateHistSet(nbins,lowbin,highbin,
                                      name+"_r",title,xaxis,
                                      tree,
                                      "(Hits_Peak[2]-roi_peak_time)",
                                      "roi_peak_charge>1&&NHits[2]>0",
                                      kBlue)
labels = ["RFFHit","CCHit","GaussHit"]
c_comp_hits_peaktime = CreateCanvas3("hits_peaktime_compare",title,labels,
                                 hists_comp_r_peaktime,hists_comp_c_peaktime,hists_comp_g_peaktime)
c_comp_hits_peaktime.Draw()

nbins=125
lowbin=-1.
highbin=1.5
name="peak_compare_mc"
title="Hits peak MC comparison"
xaxis="(Hit peak ADC - MC peak charge)/MC peak charge"
hists_comp_g_peak_mc = CreateHistSet(nbins,lowbin,highbin,
                                     name+"_g",title,xaxis,
                                     tree,
                                     "(Hits_PeakCharge[0]-MCHits_PeakCharge)/MCHits_PeakCharge",
                                     "roi_peak_charge>1&&NHits[0]>0",
                                      kBlack)
hists_comp_c_peak_mc = CreateHistSet(nbins,lowbin,highbin,
                                     name+"_c",title,xaxis,
                                     tree,
                                     "(Hits_PeakCharge[1]-MCHits_PeakCharge)/MCHits_PeakCharge",
                                     "roi_peak_charge>1&&NHits[1]>0",
                                     kRed)
hists_comp_r_peak_mc = CreateHistSet(nbins,lowbin,highbin,
                                     name+"_r",title,xaxis,
                                     tree,
                                     "(Hits_PeakCharge[2]-MCHits_PeakCharge)/MCHits_PeakCharge",
                                     "roi_peak_charge>1&&NHits[2]>0",
                                     kBlue)
labels = ["RFFHit","CCHit","GaussHit"]
c_comp_hits_peak_mc = CreateCanvas3("hits_peak_compare_mc",title,labels,
                                    hists_comp_r_peak_mc,hists_comp_c_peak_mc,hists_comp_g_peak_mc)
c_comp_hits_peak_mc.Draw()

nbins=200
lowbin=-10
highbin=10
name="peaktime_compare_mc"
title="Hits peak tick MC comparison"
xaxis="(Hit peak tick - MC peak tick)"
hists_comp_g_peaktime_mc = CreateHistSet(nbins,lowbin,highbin,
                                         name+"_g",title,xaxis,
                                         tree,
                                         "(Hits_Peak[0]-MCHits_Peak)",
                                         "roi_peak_charge>1&&NHits[0]>0",
                                         kBlack)
hists_comp_c_peaktime_mc = CreateHistSet(nbins,lowbin,highbin,
                                         name+"_c",title,xaxis,
                                         tree,
                                         "(Hits_Peak[1]-MCHits_Peak)",
                                         "roi_peak_charge>1&&NHits[1]>0",
                                         kRed)
hists_comp_r_peaktime_mc = CreateHistSet(nbins,lowbin,highbin,
                                         name+"_r",title,xaxis,
                                         tree,
                                         "(Hits_Peak[2]-MCHits_Peak)",
                                         "roi_peak_charge>1&&NHits[2]>0",
                                         kBlue)
labels = ["RFFHit","CCHit","GaussHit"]
c_comp_hits_peaktime_mc = CreateCanvas3("hits_peaktime_compare_mc",title,labels,
                                        hists_comp_r_peaktime_mc,hists_comp_c_peaktime_mc,hists_comp_g_peaktime_mc)
c_comp_hits_peaktime_mc.Draw()

nbins=19
lowbin=-9.5
highbin=9.5
name="nhits_compare_mc"
title="NHits comparison"
xaxis="(N_{Reco} - N_{Sim})"
hists_comp_g_nhits_mc = CreateHistSet(nbins,lowbin,highbin,
                                      name+"_g",title,xaxis,
                                      tree,
                                      "(NHits[0]-NMCHits)",
                                      "1",
                                      kBlack)
hists_comp_c_nhits_mc = CreateHistSet(nbins,lowbin,highbin,
                                      name+"_c",title,xaxis,
                                      tree,
                                      "(NHits[1]-NMCHits)",
                                      "1",
                                      kRed)
hists_comp_r_nhits_mc = CreateHistSet(nbins,lowbin,highbin,
                                      name+"_r",title,xaxis,
                                      tree,
                                      "(NHits[2]-NMCHits)",
                                      "1",
                                      kBlue)
labels = ["RFFHit","CCHit","GaussHit"]
c_comp_nhits_mc = CreateCanvas3("nhits_compare_mc",title,labels,
                                hists_comp_r_nhits_mc,hists_comp_c_nhits_mc,hists_comp_g_nhits_mc)
c_comp_nhits_mc.Draw()


nbins=200
lowbin=-2
highbin=2
name="time_compare_mc"
title="Hits average time MC comparison"
xaxis="(Hit average time - MC average time)"
hists_comp_g_time_mc = CreateHistSet(nbins,lowbin,highbin,
                                     name+"_g",title,xaxis,
                                     tree,
                                     "(Hits_wAverageTime[0]-MCHits_wAverageTime)",
                                     "roi_peak_charge>1&&NHits[0]>0",
                                     kBlack)
hists_comp_c_time_mc = CreateHistSet(nbins,lowbin,highbin,
                                     name+"_c",title,xaxis,
                                     tree,
                                     "(Hits_wAverageTime[1]-MCHits_wAverageTime)",
                                     "roi_peak_charge>1&&NHits[1]>0",
                                     kRed)
hists_comp_r_time_mc = CreateHistSet(nbins,lowbin,highbin,
                                     name+"_r",title,xaxis,
                                     tree,
                                     "(Hits_wAverageTime[2]-MCHits_wAverageTime)",
                                     "roi_peak_charge>1&&NHits[2]>0",
                                     kBlue)
labels = ["GaussHit","CCHit","RFFHit"]
c_comp_hits_time_mc = CreateCanvas3("hits_time_compare_mc",title,labels,
                                    hists_comp_g_time_mc,hists_comp_c_time_mc,hists_comp_r_time_mc)
c_comp_hits_time_mc.Draw()

nbins=200
lowbin=-3
highbin=5
name="integral_compare"
title="Hits integral comparison"
xaxis="(Hit ADC integral - ROI ADC integral)/ROI ADC integral"
hists_comp_g_integral = CreateHistSet(nbins,lowbin,highbin,
                                      name+"_g",title,xaxis,
                                      tree,
                                      "(Hits_IntegratedCharge[0]-roi_charge)/roi_charge",
                                      "roi_peak_charge>1",
                                      kBlack)
hists_comp_c_integral = CreateHistSet(nbins,lowbin,highbin,
                                      name+"_c",title,xaxis,
                                      tree,
                                      "(Hits_IntegratedCharge[1]-roi_charge)/roi_charge",
                                      "roi_peak_charge>1",
                                      kRed)
hists_comp_r_integral = CreateHistSet(nbins,lowbin,highbin,
                                      name+"_r",title,xaxis,
                                      tree,
                                      "(Hits_IntegratedCharge[2]-roi_charge)/roi_charge",
                                      "roi_peak_charge>1",
                                      kBlue)
labels = ["CCHit","GaussHit","RFFHit"]
c_comp_hits_integral = CreateCanvas3("hits_integral_compare",title,labels,
                                     hists_comp_c_integral,hists_comp_g_integral,hists_comp_r_integral)
c_comp_hits_integral.Draw()

nbins=150
lowbin=-1
highbin=2
name="integral_compare_mc"
title="Hits integral MC comparison"
xaxis="(Hit ADC integral - MC charge integral)/MC charge integral"
hists_comp_g_integral_mc = CreateHistSet(nbins,lowbin,highbin,
                                      name+"_g",title,xaxis,
                                      tree,
                                      "(Hits_IntegratedCharge[0]-MCHits_IntegratedCharge)/MCHits_IntegratedCharge",
                                      "roi_peak_charge>1",
                                      kBlack)
hists_comp_c_integral_mc = CreateHistSet(nbins,lowbin,highbin,
                                      name+"_c",title,xaxis,
                                      tree,
                                      "(Hits_IntegratedCharge[1]-MCHits_IntegratedCharge)/MCHits_IntegratedCharge",
                                      "roi_peak_charge>1",
                                      kRed)
hists_comp_r_integral_mc = CreateHistSet(nbins,lowbin,highbin,
                                      name+"_r",title,xaxis,
                                      tree,
                                      "(Hits_IntegratedCharge[2]-MCHits_IntegratedCharge)/MCHits_IntegratedCharge",
                                      "roi_peak_charge>1",
                                      kBlue)
labels = ["CCHit","GaussHit","RFFHit"]
c_comp_hits_integral_mc = CreateCanvas3("hits_integral_compare_mc",title,labels,
                                     hists_comp_c_integral_mc,hists_comp_g_integral_mc,hists_comp_r_integral_mc)
c_comp_hits_integral_mc.Draw()

finalinput = raw_input("Hit enter to exit.")
sys.exit()
