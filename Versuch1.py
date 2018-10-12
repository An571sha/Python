#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 15:19:48 2018

@author: animesh
"""
""" Mittelwert und standardabweichung berechnen 
"""
import numpy as np
import csv  


filename = "Messung1.csv"
reader = csv.reader(open("Messung1.csv","r" ), delimiter=",")
for row in enumerate(reader):
    print(row)

    
    