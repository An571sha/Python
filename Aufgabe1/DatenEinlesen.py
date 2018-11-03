#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 16:20:58 2018

@author: animesh
"""
import numpy as np;
import matplotlib.pyplot as p;
import glob
import os;
#source1 = open("/Users/animesh/Desktop/Python/Aufgabe1/abgabe1/a1_10cm.csv")
#source2 = open("/Users/animesh/Desktop/Python/Aufgabe1/abgabe1/a1_10cm.csv")
#Spannung = np.genfromtxt(source1, delimiter= ",", skip_header=1000, usecols = (4))
#Zeit = np.genfromtxt(source2, delimiter= ",", skip_header=1000, usecols = (3))
#print (Spannung);

#NS = len(Spannung)
#mittelwert = sum(Spannung)/NS
#standardabweichung = np.sqrt(sum((Spannung-mittelwert)**2)/(NS-1));
i = 0
arrayMittelwert = [0]*20
arrayDis = [10,11,12,13,15,17,19,22,24,27,30,32,36,40,43,50,55,60,66,70]
weg = os.path.join("/Users/animesh/Desktop/Python/Aufgabe1/abgabe1", "*.csv")

for filename in glob.glob(weg):
    Spannung = np.genfromtxt(filename , delimiter= ",", skip_header=1000, usecols = (4))
    NS = len(Spannung)
    mittelwert = sum(Spannung)/NS
    standardabweichung = np.sqrt(sum((Spannung-mittelwert)**2)/(NS-1));
    arrayMittelwert[i] = mittelwert
    i = i+1

print("mittelwert:{}".format(mittelwert))
print("standardabweichung:{}".format(standardabweichung))
    

p.plot(arrayDis,arrayMittelwert)
p.show()