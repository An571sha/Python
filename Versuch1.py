#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 15:19:48 2018

@author: animesh
"""
""" Mittelwert und standardabweichung berchnen 
"""
import numpy as np
import csv
filename = "Messung1.txt"
reader = csv.reader(open("Messung1.txt","rb" ), delimiter=",")
for row in reader:
    print(row)
    