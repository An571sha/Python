#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:10:18 2018

@author: animesh
"""
import numpy as np;
import matplotlib.pyplot as p;

filename = open("/Users/animesh/Desktop/Python/Aufgabe1/abgabe3/dina4_laenge.csv",)
Spannung = np.genfromtxt(filename , delimiter= ",", skip_header=1000, usecols = (4))
NS = len(Spannung)
mittelWert = sum(Spannung)/NS
Lengthexact = 29.7
standardabweichung = np.sqrt(sum((Spannung-mittelWert)**2)/(NS-1));
logSpannung = np.log(mittelWert)
meanLogSpannung = np.mean(logSpannung)

#Korekkte Angabe des Messergebninss in sicherheit von 68.28%
x1 = mittelWert +(standardabweichung)
x2 = mittelWert -(standardabweichung)

#Korekkte Angabe des Messergebninss in sicherheit von 95%

x3 = mittelWert +((standardabweichung)*1.96)
x4 = mittelWert -((standardabweichung)*1.96)


#Formel einsetzen
a1=(logSpannung + meanLogSpannung)*(Length-Lengthexact) #sum (x - Mx)(Length)
a2=pow((logSpannung + meanLogSpannung),2)   #sum(x-Mx)^2

a = a1/a2                     
b = Length - a*meanLogSpannung    
print(a)
print(b)


y = ([np.exp(a * logSpannung + b)])
p.plot(Length,y)
p.show()