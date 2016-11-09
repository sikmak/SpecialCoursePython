# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:02:00 2016

@author: Никита
"""
from math import pi

r=10.6
a=1.3
b=1
S_circle=pi*r**2
S_rectangle=a
while S_circle > S_rectangle:
    S_rectangle=a*b
    b+=1
print(b)