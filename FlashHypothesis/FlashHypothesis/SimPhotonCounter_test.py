from ROOT import opdet
from ROOT.opdet import FlashHypothesis,FlashHypothesisCollection
#from ROOT.opdet import FlashHypothesisCalculator
from ROOT import sim
from ROOT.sim import OnePhoton,SimPhotons
from ROOT.opdet import SimPhotonCounter

from ROOT import vector,map

counter = SimPhotonCounter()
counter.Print()
print "======================"

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

