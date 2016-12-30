# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 19:00:41 2016

@author: Никита
"""
import os
from numpy import random

N=int(input("Введите N:"))
x=[]
M=0
vrem=0
for i in range(N):
    vrem=random.randint(1,7)
    x.append(vrem)
    if vrem==6:
        M+=1.
print("Вероятность:")
print(str(M/N))
print("Все варианты:")
print(x)
os.system("pause")
