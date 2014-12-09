from ROOT import *
import sys

file_name = "/Users/wketchum/MicroBooNE_Data/hitana_muons_rff.root"

myfile = TFile(file_name,"READ")
mydir  = myfile.Get("hitana")
mytree  = mydir.Get("wireDataTree")



mytree.StartViewer()

finalinput = raw_input("Hit enter to exit.")

sys.exit()
