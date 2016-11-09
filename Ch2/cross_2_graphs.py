# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:14:30 2016

@author: Никита
"""
from numpy import linspace
N = float(input("Введите N: "))
E= float(input("Введите эпсилон: "))

x = linspace(-4,4,N)
i=0;
while i<N:
    if abs(x[i]-x[i]**2) < E:
        print(x[i])
        break
    i+=1

if i==N:
    print("Значения не нашлось")