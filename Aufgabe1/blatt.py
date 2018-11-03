#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:10:18 2018

@author: animesh
"""
import numpy as np;
import matplotlib.pyplot as p;

#Die csv Datei einlesen-------------------------------------------------------------------------------------------------------

filename1 = open("/Users/animesh/Desktop/Python/Aufgabe1/abgabe3/dina4_laenge.csv",)
filename2 = open("/Users/animesh/Desktop/Python/Aufgabe1/abgabe3/dina4_breite.csv",)
SpannungLaenge = np.genfromtxt(filename1 , delimiter= ",", skip_header=1000, usecols = (4))
SpannungBreite = np.genfromtxt(filename2 , delimiter= ",", skip_header=1000, usecols = (4))

#Laenge-----------------------------------------------------------------------------------------------------------------------

NSL = len(SpannungLaenge)
mittelWertLaenge = sum(SpannungLaenge)/NSL
Lengthexact = 29.7
standardabweichungL = np.sqrt(sum((SpannungLaenge-mittelWertLaenge)**2)/(NSL-1));
logSpannungLaenge = np.log(mittelWertLaenge)
meanLogSpannung = np.mean(logSpannungLaenge)

#Breite-----------------------------------------------------------------------------------------------------------------------

NSB = len(SpannungBreite)
mittelWertBreite = sum(SpannungBreite)/NSB
Breathexact = 29.7
standardabweichungB = np.sqrt(sum((SpannungBreite-mittelWertBreite)**2)/(NSB-1));
logSpannungBreite = np.log(mittelWertBreite)
meanLogBreite = np.mean(logSpannungBreite)


#Formel einsetzen-------------------------------------------------------------------------------------------------------------

a = -1.7083868215513274
b = 2.7784983876002296 
yL = ((np.exp(a * logSpannungLaenge + b)))
yB = ([np.exp(a * logSpannungBreite + b)])

#Korrektur----------------------------------------------68%
Laenge1 = mittelWertLaenge + (1.0 * standardabweichungL)
Laenge2 = mittelWertLaenge - (1.0 * standardabweichungL)
Breite1 = mittelWertBreite + (1.0 * standardabweichungL)
Breite2 = mittelWertBreite - (1.0 * standardabweichungL)

#korrektur----------------------------------------------95%
Laenge3 = mittelWertLaenge + (1.98 * standardabweichungL)
Laenge4 = mittelWertLaenge - (1.98 * standardabweichungL)
Breite3 = mittelWertBreite + (1.98 * standardabweichungL)
Breite4 = mittelWertBreite - (1.98 * standardabweichungL)

#Ableiten und Korrektur-------------------------------------------------------------------------------------------------------

yL1 = -(a+1)*((np.exp(b))*((Laenge1)**(a)))
yL2 = -(a+1)*((np.exp(b))*((Laenge2)**(a)))
yB1 = -(a+1)*((np.exp(b))*((Breite1)**(a)))
yB2 = -(a+1)*((np.exp(b))*((Breite2)**(a)))
yL3 = -(a+1)*((np.exp(b))*((Laenge3)**(a)))
yL4 = -(a+1)*((np.exp(b))*((Laenge4)**(a)))
yB3 = -(a+1)*((np.exp(b))*((Breite3)**(a)))
yB4 = -(a+1)*((np.exp(b))*((Breite4)**(a)))

print(yL1)
print(yL2)
print(yB1)
print(yB2)
print(yL3)
print(yL4)
print(yB3)
print(yB4)

