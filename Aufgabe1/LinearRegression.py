#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:04:29 2018

@author: animesh
"""
import numpy as np;
import matplotlib.pyplot as p;
import glob
import os;

arrayDis = [10,11,12,13,15,17,19,22,24,27,30,32,36,40,43,50,55,60,66,70]
arrayMittelWert = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i=0

#Die Daten aus CSV Datei holen---------------------------------------------------------------------------------------------

for filename in glob.glob(os.path.join("/Users/animesh/Desktop/Python/Aufgabe1/abgabe1", "*.csv")):
    Spannung = np.genfromtxt(filename , delimiter= ",", skip_header=1000, usecols = (4))
    NS = len(Spannung)
    mittelwert = sum(Spannung)/NS
    arrayMittelWert[i]= mittelwert
    i = i+1
#Logartimieren und plotten--------------------------------------------------------------------------------------------------------

logSpannung = np.log(arrayMittelWert)
logdist = np.log(arrayDis) 
    
print(logSpannung)
print(logdist)
p.plot(logdist,logSpannung)
p.show()    


meanLogSpannung = np.mean(logSpannung)
meanLogDist = np.mean(logdist)

print(meanLogSpannung)
print(meanLogDist)

#Formel einsetzen--------------------------------------------------------------------------------------------------------------

a1=0
a2=0
for i in range(len(logSpannung)):
    a1+=(logSpannung[i]-meanLogSpannung)*(logdist[i]- meanLogDist) #sum (x - Mx)(y-My)
    a2+=pow((logSpannung[i]-meanLogSpannung),2)                    #sum(x-Mx)^2

a = a1/a2                     
b = meanLogDist - a*meanLogSpannung                                #b = y - a*x

print("a:",a)
print("b:",b)    

#x = arrayDis
#y = (np.exp(a*x+b) for x in logSpannung)
#p.plot(x,y)
#p.show()
fig, ax = p.subplots()
ax.plot([np.exp(a * x + b) for x in logSpannung], arrayDis)
