# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:20:20 2016

@author: Никита
"""

def everage(N):
    n=N/2;
    print(n)
    if isinstance( n, int ):
         return n-.5
    else:
        return n+.5

N = int(input("Введите N: "))
print("Среднее значение = "+str(everage(N)))
