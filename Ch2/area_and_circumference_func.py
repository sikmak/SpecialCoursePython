# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:32:55 2016

@author: Никита
"""
import os
from math import pi

def cuircle_square(r):
    S = pi*r**2
    return S
    
def cuircle_length(r):
     L = 2*pi*r
     return L
    
r=float(input("Введите радиус окружности: "))
print("Длина окружности: "+str(cuircle_length(r))+"\n")
print("Площадь круга: "+str(cuircle_square(r)))
os.system("pause")
