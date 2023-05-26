##File used in the analysis note
##Comparison between nvelo=1 and nvelo=2 and nvelo==3 dielectron samples

from __future__ import print_function
import sys, os
import ROOT
from ROOT import *
from array import array
from ctypes import *
import numpy as np
from scipy.interpolate import interp1d


def mk_limit(fname="",m=-1,minm=-1,maxm=-1,hname="",xtitle="",rebin=1):
  flbl    = TFile(inputdir+"/superchic/lbl/plots.root","read")
  fdie    = TFile(inputdir+"/MC_DiElectron/plots.root","read")
  falp    = TFile(fname)
  h1_die  = fdie.Get("ACO_APT_NP2_NV2_l0eff/"+hname)
  h1_lbl  = flbl.Get("digammaM_fastsim")
  h1_alp  = falp.Get("ACO_APT_NP2_NV0_l0eff/"+hname)

  h1_lbl.Rebin(rebin) 
  h1_die.Rebin(rebin)
  h1_alp.Rebin(rebin)

  h1_lbl.Scale(wlbl)
  h1_die.Scale(nexpdie/h1_die.Integral())
  h1_lbl.Add(h1_die)
  h1_alp.Scale(walp)

  
  
  #h1_alp.Scale(0.5*h1_lbl.GetMaximum()/h1_alp.GetMaximum())

  legend = TLegend(0.75,0.75,0.92,0.92)
  legend.SetFillColor(0)
  legend.SetTextSize(0.032)
  legend.AddEntry(h1_die, "ee", "fl")
  legend.AddEntry(h1_lbl, "ee+lbl", "l")

  h1_alp.SetLineColor(kRed)
  h1_die.SetFillColor(kGray)

  h1_lbl.Draw("hist")
  h1_die.Draw("hist same")
  h1_alp.Draw("hist same")

  legend.Draw("same")
  c1.SetLogy(0)
  c1.SetGridy(1)
  c1.SetGridx(1)
  c1.Print(savedir+tag+"_"+hname+"_"+str(m)+".pdf")
  c1.Print(savedir+tag+"_"+hname+"_"+str(m)+".gif")
  c1.SetLogy(1)
  c1.Print(savedir+tag+"_"+hname+"_"+str(m)+"_log.pdf")
  c1.Print(savedir+tag+"_"+hname+"_"+str(m)+"_log.gif")
  c1.SetLogy(0)

  cls, galp = array('d'), array('d')
  g_range = np.linspace(5., 1.9, 100)
  for g in g_range:
  #for g in [5., 4.7, 4.4, 4.1, 2., 1.7, 1.1, .5, .2]:
    h1_alp.Scale(g*g)
    h1_die.Scale(3./h1_die.Integral())
    mydatasource = TLimitDataSource(h1_alp,h1_lbl,h1_die)
    myconfidence = ROOT.TLimit.ComputeLimit(mydatasource,50000)
    cls.append(myconfidence.GetExpectedCLs_b()) #<CLs>
    galp.append(g)
    h1_alp.Scale(1./(g*g)) #scale back to standard cross-section
    
  h1b = TH1F("h1b","",1,0,galp[0])
  h1b.Fill(2,0.05)
  gr_cls_galp = ROOT.TGraph(100, galp, cls)
  gr_cls_galp.SetMarkerSize(0.7)
  gr_cls_galp.SetMarkerStyle(ROOT.kFullCircle)
  gr_cls_galp.SetMarkerColor(kBlack)
  h1b.GetXaxis().SetTitle("g_{a#gamma} #times 10^{-4}") #galp_norm = 1e-4
  h1b.GetYaxis().SetTitle("CLs")
  h1b.Draw("hist")
  h1b.SetLineColor(kRed)
  h1b.GetYaxis().SetRangeUser(0,1)
  gr_cls_galp.Draw("p")
  c1.SetLogy(0)
  c1.Print(savedir+tag+"_cls_"+str(m)+".pdf")
  c1.Print(savedir+tag+"_cls_"+str(m)+".gif")

  f = interp1d(cls, galp, kind = 'cubic')
  cls_up = .05
  galp_up = f(cls_up)

  return galp_up





ROOT.gROOT.SetBatch(True)

total = len(sys.argv)
cmdargs = str(sys.argv)
print ("The total numbers of args passed to the script: %d " % total)

gROOT.ProcessLine(".x include/lhcbstyle.C")
gStyle.SetOptStat(0)
gStyle.SetMarkerStyle(20)
gStyle.SetMarkerSize(1.5)

inputdir    = "./"
savedir     = "./"

lumi    = 0.216 #1/nb
csdie   = 2.68e6 #nb
ngendie = 4e6 #4M events generated
nexpdie = 0.42 #expected number of events due to lack of events after selection requirements
cslbl   = 13721 #nb
ngenlbl = 700e3 #700k events generated
wlbl    = lumi*cslbl / ngenlbl 
walp    = 1 #calculated below in the loop

tag         = "limits"
#os.makedirs(savedir, exist_ok = True)
#fsave       = TFile(savedir+"plots.root","recreate");

# create canvas
canvasWidth  = 800
canvasHeight = 600
c1 = TCanvas("eff","",canvasWidth,canvasHeight)

minpt=0.1
maxpt=4
rebin=2

list_mc   = ["ALP2.5GeV","ALP3GeV","ALP4GeV","ALP5GeV","ALP6GeV","ALP7GeV","ALP8GeV","ALP9GeV","ALP10GeV"]
list_mass = {"ALP2.5GeV": 2.5, "ALP3GeV": 3.0, "ALP4GeV": 4.0, "ALP5GeV": 5.0, "ALP6GeV": 6.0, "ALP7GeV": 7.0, "ALP8GeV": 8.0, "ALP9GeV": 9.0, "ALP10GeV": 10.0}
list_cs   = {"ALP2.5GeV": 0.1272908E+05, "ALP3GeV": 0.1274609E+05, "ALP4GeV": 8734062./1e3, "ALP5GeV": 7167724./1e3, "ALP6GeV": 7170942./1e3, "ALP7GeV": 6206022./1e3, "ALP8GeV": 5440195./1e3, "ALP9GeV": 4821581./1e3, "ALP10GeV": 4308322./1e3}
#list_mc   = ["ALP2GeV","ALP2.5GeV","ALP3GeV","ALP4GeV","ALP5GeV","ALP6GeV","ALP7GeV","ALP8GeV","ALP9GeV","ALP10GeV"]
#list_mass = {"ALP2GeV": 2.0, "ALP2.5GeV": 2.5, "ALP3GeV": 3.0, "ALP4GeV": 4.0, "ALP5GeV": 5.0, "ALP6GeV": 6.0, "ALP7GeV": 7.0, "ALP8GeV": 8.0, "ALP9GeV": 9.0, "ALP10GeV": 10.0} 
#cross section is for coupling 1e-3
#list_cs   = {"ALP2GeV": 0.1496774E+05, "ALP2.5GeV": 0.1272908E+05, "ALP3GeV": 0.1274609E+05, "ALP4GeV": 8734062./1e3, "ALP5GeV": 7167724./1e3, "ALP6GeV": 7170942./1e3, "ALP7GeV": 6206022./1e3, "ALP8GeV": 5440195./1e3, "ALP9GeV": 4821581./1e3, "ALP10GeV": 4308322./1e3} 
galp_norm = 1e-4

ngen = [#2051006, #2GeV
        2049686, #2.5GeV
        2036652, #3GeV
        2713257, #4GeV
        2293087, #5GeV
        2055123, #6GeV 
        2237143, #7GeV
        2204730, #8GeV
        2205091, #9GeV
        2164133, #10GeV
        ]  #number of MC generated events


mass, galps = array('d'), array ('d')



for (i, mc) in enumerate(list_mc):
  walp = lumi*list_cs[mc] / ngen[i] * (galp_norm*galp_norm)/(1e-3*1e-3) #coupling 1e-4
  galp_up = mk_limit(inputdir+"/MC_"+mc+"/plots.root",list_mass[mc],0,12.,"h1_digammaM","M (#gamma#gamma) [GeV]", 40)
  galps.append(galp_up*1e-1) #TeV-1
  mass.append(list_mass[mc])


for i in range(len(galps)):
  print(galps[i], mass[i])
  
#for x, y in zip(galps, mass):
#  print(x,y)



c2 = TCanvas("c2", "Exclusion plot", 800, 600)
c2.SetLogy()
c2.SetLogx()
#c2.SetGrid()

frame = TH2F("frame","",10,0.001,5000,10,0.0067,40)
frame.GetXaxis().SetTitle('m_{a} GeV')
#frame.GetYaxis().SetTitle('g_{a#gamma} #times 10^{-4} GeV^{-1}') #galp_norm = 1e-4
frame.GetYaxis().SetTitle('g_{a#gamma} #times TeV^{-1}')
frame.Draw()

galp_up_mass = TGraph(9, mass, galps)
#galp_up_mass.SetMarkerColor(4)
#galp_up_mass.SetMarkerSize(.8)
galp_up_mass.SetLineColor(6)
galp_up_mass.SetLineWidth(603)
galp_up_mass.SetFillStyle(3003)
galp_up_mass.SetFillColor(6)
galp_up_mass.Draw('L')


c2.Print("galp_mass.png")


print("done")



#import matplotlib
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt

#plt.loglog(mass,1e-1*galps,marker = "o")
#plt.savefig("galp_x_mass.png")


