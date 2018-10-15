#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 20:17:06 2018

@author: animesh
"""
import numpy as np
import numpy.polynomial.polynomial as po
import matplotlib.pyplot as plt

#Eine Mehode um gerade linie in der graph zu plotten
def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals # y = b + mx
    plt.plot(x_vals, y_vals)

slope = 4;
intercept = 0;

abplot = abline(slope,intercept);

######------
#linear_regression
xeintraege = np.array[10,20,30,40,50,60,70,80]
yeintaege = np.array[20,40,60,80,100,120,140]
