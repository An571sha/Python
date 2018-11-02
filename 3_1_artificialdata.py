#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:19:41 2018

@author: axtr
"""
import numpy as np
from numpy import random
import matplotlib.pyplot as plt


#------------------------------------------------------------------------
# Funktion erzeugt kuenstiliche Messdaten
# R Datenreihen a N Messungen 
def adata(xw,N,alpha,R):
    admat = np.zeros((N,R))

    for j in range(R):
        admat[:,j] = xw+alpha*(2*random.rand(N)-1);
        
    return admat;

#------------------------------------------------------------------------
R  = 1000;                        # Anzahl Messreihen
N  = 1000;                       # Anzahl Messungen einer Reihe
xw = 20;                        # exakter Wert
alpha = 0.5;                    # Streubereich


#------------------------------------------------------------------------
# kuenstliche Messdaten erzeugen R Serien mit jeweils N Messungen
admat = adata(xw,N,alpha,R);

#------------------------------------------------------------------------
#

# Mittelwert bestimmen
xM   = sum(admat)/N;
# Standardabweichung
sig  = np.sqrt(sum((admat-xM)**2)/(N-1));
# Standardfehler des Mittelwerts
sigE = sig/np.sqrt(N);

#------------------------------------------------------------------------
# Visualisation
plt.figure(figsize=(12,8))


if R<=10 and N<=100:
    plt.subplot(3,1,1)
    for j in range(R):
        plt.plot(admat[:,j],'.')
plt.subplot(3,1,2)
plt.hist(xM,bins=30)
plt.subplot(3,2,5)
plt.plot(sig,'mo')
plt.xlabel('Messreihe')
plt.ylabel('Standardabweichung')
plt.subplot(3,2,6)
plt.plot(xM,'ko')
plt.xlabel('Messreihe')
plt.ylabel('Mittelwert')
#plt.plot(sigE,'ko')
#plt.xlabel('Messreihe')
#plt.ylabel('sigE')
plt.show()

