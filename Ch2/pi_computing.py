# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:44:01 2016

@author: Никита
"""
import os
from numpy import zeros
from math import pi,sqrt
import matplotlib.pyplot as plt

def Leibnitc(N):
    x=zeros(N)
    vrem2=0
    for i in range(N):
        vrem=(4*i+1)*(4*i+3)
        vrem2+=8/vrem
        x[i]=pi-vrem2
    print("Погрешность N-ого эл-та по Лейбницу:"+str(x[N-1]))
    return x
def Eiler(N):
    x=zeros(N)
    vrem2=0
    x[0]=0
    for i in range(1,N,1):
        vrem=i**2
        vrem2+=6/vrem
        x[i]=pi-sqrt(vrem2)
    print("Погрешность N-ого эл-та по Эйлеру:"+str(x[N-1]))
    return x

N = int(input("Введите N:"))
y = zeros(N)

for i in range(N):
    y[i]=i

plt.ylabel('E(N)')
plt.plot(y,Leibnitc(N))
plt.plot(y,Eiler(N))
plt.show()
os.system("pause")
