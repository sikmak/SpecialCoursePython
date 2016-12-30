# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 19:20:20 2016

@author: Никита
"""
import os
def everage(N):
    print("i=1")
    print("Среднее значение равно:1")
    for i in range(2,N+1):
        n=i/2.;
        print("i="+ str(i))
        if isinstance( n, int ):
            print("Среднее значение равно:"+str(n-.5))
        else:
            print("Среднее значение равно:"+str(n+.5))

N = int(input("Введите N: "))
everage(N)
os.system("pause")
