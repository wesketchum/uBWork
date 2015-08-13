from ROOT import RawDigitAdder
from ROOT import std
from ROOT.std import vector


import unittest
import sys

class TestRawDigitAdderClass(unittest.TestCase):
    def setUp(self):
        self.rda = RawDigitAdder(False)
        self.wave3 = vector('short')()
        self.wave3 += [0,-1,10,-2,0]
        self.wave1 = vector('short')()
        self.wave1 += [0,1,0,3,9,4,1,2,0,1]
        self.wave2 = vector('short')()
        self.wave2 += [1,1,8,22,15,2,0,0,1,3]
        self.wave1pwave2 = vector('short')()
        self.wave1pwave2 += [1,2,8,25,24,6,1,2,1,4]
        self.orig_wave1=self.wave1
        self.orig_wave2=self.wave2
        self.orig_wave3=self.wave3

    def test_name(self):
        self.assertEqual(self.rda.Name(),"RawDigitAdder_Base")

    def test_diff_sizes(self):
        self.rda.AddRawDigits(self.wave1,self.wave3)
        self.assertEqual(self.orig_wave1,self.wave1)
        self.assertEqual(self.orig_wave2,self.wave2)
        self.assertEqual(self.orig_wave3,self.wave3)

    def test_base_adder_3arg(self):
        self.rda.AddRawDigits(self.wave1,self.wave2,self.wave3)
        self.assertEqual(self.wave3.size(),10)
        for x in range(0,10):
            self.assertEqual(self.wave3[x],self.wave1pwave2[x])
            self.assertEqual(self.orig_wave1[x],self.wave1[x])
            self.assertEqual(self.orig_wave2[x],self.wave2[x])
                                
    def test_base_adder_2arg(self):
        self.rda.AddRawDigits(self.wave1,self.wave2)
        self.assertEqual(self.wave2.size(),10)
        self.assertEqual(self.wave2,self.wave1pwave2)
        self.assertEqual(self.orig_wave1,self.wave1)

    def test_base_adder_list(self):
        waveList = vector(vector('short'))()
        waveList.push_back(self.wave1)
        waveList.push_back(self.wave2)
        self.rda.AddRawDigits(waveList,self.wave3)
        self.assertEqual(self.wave2.size(),10)
        for x in range(0,10):
            self.assertEqual(self.wave3[x],self.wave1pwave2[x])
            self.assertEqual(self.orig_wave1[x],self.wave1[x])
            self.assertEqual(self.orig_wave2[x],self.wave2[x])

    def test_base_adder_neg(self):
        wave_neg = vector('short')(10,-1000)
        wave_max = vector('short')(10,32767)
        self.rda.AddRawDigits(self.wave1,wave_neg)
        self.assertEqual(wave_neg.size(),10)
        self.assertEqual(wave_neg,wave_max)
        self.assertEqual(self.orig_wave1,self.wave1)

                    
if __name__ == '__main__':
    unittest.main()
