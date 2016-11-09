# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 13:19:07 2016

@author: Никита
"""

import matplotlib.pyplot as plt

def error(a,b,x,y):
    e=0
    for i in range(5):
        e+=(a*x[i]+b-y[i])**2
    return e
    
def f(a,b,x):
    y=[]
    for i in range(len(x)):
        y.append(a*x[i]+b)
    return y;
    
y=[0.5,2.0,1.0,1.5,7.5]
x=[0,1,2,3,4]
flag=1
while flag==1:
    a=float(input("Введите значение a:"))
    b=float(input("Введите значение b:"))
    print(error(a,b,x,y))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x,f(a,b,x))
    plt.plot(x,y)
    plt.show()
    flag=int(input('''Если Вас утраивает погрешность наберите 0
                   Иначе нажмите 1:\n'''))