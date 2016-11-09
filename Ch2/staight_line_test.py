# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:45:56 2016

@author: Никита
"""
from numpy import random

c=2
a=float(input("Введите нижнюю границу промежутка:\n"))
b=float(input("Введите верхнюю границу промежутка:\n"))
x=[]
for i in range(100):
    x.append(random.uniform(a,b))
a=(4*x[0]-4*c)/(x[0]-c)
for i in range(99):
    a2=(4*x[i+1]-4*c)/(x[i+1]-c)
    if a2!=a:
        print(a)
        print(a2)
        break
print("Условие прямоты выполнено\n")