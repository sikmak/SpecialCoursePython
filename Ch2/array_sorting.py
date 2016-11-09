# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:26:22 2016

@author: Никита
"""
from random import *
from numpy import sort,zeros

x = zeros(6);
for i in range(6):
    x[i] = uniform(0, 10)
print(x)
x = sort(x)
print(x)
