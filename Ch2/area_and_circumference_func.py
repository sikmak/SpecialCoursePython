# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 16:32:55 2016

@author: Никита
"""
from math import pi

def cuircleLength_square(r):
    C = 2.*pi*r
    A = 2*pi*r**2
    return C,A
    
    
r=float(input("Введите радиус окружности: "))
print("Длина окружности, Площадь окружности:")
print(cuircleLength_square(r))