#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 14:08:16 2018

@author: animesh
"""
import numpy as np;
from numpy import random;


def adata(xw,N,alpha,R):
    admat = np.zeros((N,R))
    
    for j in range(R):
        admat[:,j] = xw + alpha*(random(0,N)-1);
        
    return admat;

R = 4;
xw = 20;
N = 1000;
alpha = 0.5

admat = adata(xw,N,alpha,R);

xM = sum(admat)/N;

standardabweichung = np.sqrt(sum((admat-xM)**2)/(N-1));