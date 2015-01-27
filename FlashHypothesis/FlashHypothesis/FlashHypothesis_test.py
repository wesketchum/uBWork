from ROOT import opdet
from ROOT.opdet import FlashHypothesis,FlashHypothesisCollection
from ROOT.opdet import FlashHypothesisCalculator

from ROOT import vector

print "\n======================================="
print "FlashHypothesis Checks"

my_prompt_vec = vector('float')(3)
my_prompt_vec[0]=9
my_prompt_vec[1]=16
my_prompt_vec[2]=25
my_prompt_hyp = FlashHypothesis(my_prompt_vec)

my_prompt_hyp.Print()

my_late_vec = vector('float')(3)
my_late_vec[0]=my_prompt_vec[0]*2
my_late_vec[1]=my_prompt_vec[1]*2
my_late_vec[2]=my_prompt_vec[2]*2
my_late_hyp = FlashHypothesis(my_late_vec)

my_late_hyp.Print()

print "\n======================================="
print "FlashHypothesisCollection Checks"

my_collection = FlashHypothesisCollection(my_prompt_hyp,my_late_hyp)
my_collection.Print()
print "---------------"

my_collection.SetPromptHypAndPromptFraction(my_prompt_hyp,0.5);
my_collection.Print()
print "---------------"

my_collection.SetTotalHypAndPromptFraction(my_prompt_hyp,0.25);
my_collection.Print()
print "---------------"

from ROOT import TVector3

print "\n======================================="
print "FlashHypothesisCalculator Checks"

calc = FlashHypothesisCalculator()

seg = vector('double')(3)
pt1 = TVector3(0.,0.,0.)
pt2 = TVector3(1.,1.,1.)

print pt1.x(),pt2.x(),pt2.Mag()

seg = calc.SegmentMidpoint(pt1,pt2,0.0)
print "(x,y,z)=(",seg[0],",",seg[1],",",seg[2],")"

seg = calc.SegmentMidpoint(pt1,pt2,5.0)
print "(x,y,z)=(",seg[0],",",seg[1],",",seg[2],")"


qe_vector = vector('float')(5,0.1)
qe_vector[2]=0.01
vis_vector = vector('float')(5,0.1)
vis_vector[3]=1
f_p = FlashHypothesis(5)
f_p.Print();
calc.FillFlashHypothesis(100,1,pt1,pt2,qe_vector,vis_vector,f_p)
f_p.Print();
print "---------------"
my_collection.SetPromptHypAndPromptFraction(f_p,0.25);
my_collection.Print()
print "---------------"
my_collection2 = FlashHypothesisCollection(5)
my_collection2.Print()
print "---------------"
my_collection2.SetPromptHypAndPromptFraction(f_p,0.5);
my_collection2.Print()
print "---------------"
my_collection3 = my_collection + my_collection2
my_collection3.Print()
print "---------------"
my_collection3.Normalize(100)
my_collection3.Print()



from ROOT import sim
from ROOT.sim import OnePhoton,SimPhotons
from ROOT.opdet import SimPhotonCounter


counter = SimPhotonCounter(5,0.0,50.0,50.0,200,100,200,0.25)
counter.Print()
print "======================"

photon = OnePhoton()

#counter.AddOnePhoton(10,photon)

photon.Time = 10
photon.Energy = 0.00000968627
counter.AddOnePhoton(1,photon)
counter.Print()
print "======================"

photon.Time = 100
counter.AddOnePhoton(3,photon)
counter.Print()
print "======================"

counter.ClearVectors()
counter.Print()
print "======================"

photons = SimPhotons()
photons.SetChannel(1)
for x in range(0,300):
    photon.Time=x
    photons.Push_back(photon)
counter.AddSimPhotons(photons)
counter.Print()
print "======================"
photons.SetChannel(2)
counter.AddSimPhotons(photons)
counter.Print()
print "======================"

from ROOT.opdet import FlashUtilities
util = FlashUtilities()

result_vector = vector('float')(5,0.0)
result = util.CompareByError(my_collection3.GetTotalHypothesis(),counter.PromptPhotonVector(),result_vector)

print result
print result_vector[0],result_vector[1],result_vector[2],result_vector[3],result_vector[4]

result_vector = vector('float')(5,0.0)
result = util.CompareByFraction(my_collection3.GetTotalHypothesis(),counter.PromptPhotonVector(),result_vector)

print result
print result_vector[0],result_vector[1],result_vector[2],result_vector[3],result_vector[4]

from ROOT import Double
mean = Double()
rms = Double()
pos_vector = vector('float')(5,4.0)
util.GetPosition(my_collection3.GetPromptHypothesis().GetHypothesisVector(),pos_vector,mean,rms)
print mean,rms

for x in range(0,5):
    pos_vector[x] = x*10
util.GetPosition(my_collection3.GetPromptHypothesis().GetHypothesisVector(),pos_vector,mean,rms)
print mean,rms
util.GetPosition(counter.PromptPhotonVector(),pos_vector,mean,rms)
print mean,rms

from ROOT import TTree,TH1F
mytree = TTree()
h_hyp_p = TH1F()
h_hyp_l = TH1F()
h_sim_p = TH1F()
h_sim_l = TH1F()
h_cmp_p = TH1F()
h_cmp_l = TH1F()

from ROOT.opdet import FlashHypothesisComparison
cmpalg = FlashHypothesisComparison()

pos_vector_y = vector('float')(5)
pos_vector_z = vector('float')(5)
for x in range(0,5):
    pos_vector_y[x] = x*10
    pos_vector_z[x] = x

cmpalg.SetOutputObjects(mytree,h_hyp_p,h_sim_p,h_cmp_p,h_hyp_l,h_sim_l,h_cmp_l,5)
cmpalg.RunComparison(100,150,my_collection3,counter,pos_vector_y,pos_vector_z)

mytree.Print()

from ROOT import TFile
f = TFile("output.root","RECREATE")
mytree.Write()
f.Close()
