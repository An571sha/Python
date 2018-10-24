#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:08:16 2018

@author: animesh
"""
import numpy as np;
from numpy import random;

#künstlice Messdaten erzeugen
def adata(xw,N,alpha,R):
    admat = np.zeros((N,R))
    
    for j in range(R):
        admat[:,j] = xw+alpha*(random.rand(N)-1);
        
    return admat;

R = 1;
xw = 2;
N = 10;
alpha = 0.5

admat = adata(xw,N,alpha,R);

#Mittelwert
xM = sum(admat)/N;
#Standardabweichung
standardabweichung = np.sqrt(sum((admat-xM)**2)/(N-1));
print(admat);
print('s:',standardabweichung)