
from ROOT import *
import numpy as np
from array import array

"""Fit no Mass do ALP, criando uma array para os parâmetros e os guardando, a serem utilizados depois na função 'total', e, após o fit da mesma, retornar os novos parâmetros gerados por esta nova função às funções originais.
Também é calculada a integral da função gaussiana presente no fit."""

gROOT.SetBatch(True)
gSystem.RedirectOutput("alpfit.txt")
arquivo2 = TFile("monitoring_alps_3GeV_100k.root", "READ")
tree2 = arquivo2.Hlt1Bs2GammaGamma.monitor_tree_twoclusters

histograma2Mass = TH1F("Mass", "Mass - Alp", 100, 0, 4400)
histogramaMassDistance = TH2F("Mass x Distance - Alp", "Mass x Distance - Alp", 100, 0, 4400, 100, 0, 9100)
histogramaMassDistance.SetContour(1000)

for i in range(0,tree2.GetEntries()):
    tree2.GetEntry(i)
    histograma2Mass.Fill(tree2.Mass)
    histogramaMassDistance.Fill(tree2.Mass, tree2.Distance)


gStyle.SetOptStat(0)

par = array('d',5*[0.])

func = TF1("func", "gaus", 2600, 3400)
func2 = TF1("func2", "pol1", 2000, 4000)
total = TF1("total", "gaus(0)+pol1(3)", 2000, 4000)

func.SetLineColor(kBlack)
func2.SetLineColor(kGreen)
total.SetLineColor(kRed)

canvas = TCanvas("Canvas", "Canvas", 800, 600)


canvas.cd()

histograma2Mass.Fit("func","0R")
histograma2Mass.Fit("func2","0R+")

par1 = func.GetParameters()
par2 = func2.GetParameters()

par[0], par[1], par[2] = par1[0], par1[1], par1[2]
par[3], par[4] = par2[0], par2[1]
total.SetParameters(par)
histograma2Mass.Draw("SAME")
histograma2Mass.Fit("total","R+")

par = total.GetParameters()

par1[0], par1[1], par1[2] = par[0], par[1], par[2]
func.SetParameters(par1)
par2[0], par2[1] = par[3], par[4]
func2.SetParameters(par2)
func.Draw("SAME")
func2.Draw("SAME")


integralgaus = func.Integral(2600,3400)
#integral2 = par[0]*par[2]*np.sqrt(2*np.pi)  #apenas para comparação de resultados
histograma2Mass.SetLineColor(kBlue)
histograma2Mass.GetXaxis().SetTitle("Mass")
histograma2Mass.GetYaxis().SetTitle("Quantity")

legend = TLegend(0.67,0.75,0.89,0.89)
legend.AddEntry(func, "Gauss", "L")
legend.AddEntry(func2, "Pol1", "L")
legend.AddEntry(total, "Total", "L")
legend.Draw()
canvas.Draw()
canvas.Print("MassAlpFit.gif")
print(f"The integral of the Gaussian is = {integralgaus}" )
#print(integral2)

canvas2 = TCanvas("Canvas2", "Canvas2", 800, 600)

canvas2.cd()

gStyle.SetPalette(kRainBow)
histogramaMassDistance.GetXaxis().SetTitle("Mass")
histogramaMassDistance.GetYaxis().SetTitle("Distance")
histogramaMassDistance.Draw("COLZ")
canvas2.Draw()
canvas2.Print("Mass_x_Distance-Alp.pdf")


