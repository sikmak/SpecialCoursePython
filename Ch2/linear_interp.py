# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:25:38 2016

@author: Никита
"""

#import matplotlib.pyplot as plt
from math import ceil

#plt.xlabel("Time")
#plt.ylabel("Y(T)")
#plt.plot(range(5),)
def interpolate(Yt,Tx):
    T1=int(Tx)
    T2=ceil(Tx)
    k=(Yt[T1-1]-Yt[T2-1])/(T1-T2)
    b=Yt[T1-1]-k*T1
    return k*Tx+b



answer = input("Введите какую задачу Вы хотите решить(а,b,c):\n")
if answer =="a":
    Tx = float(input("Ввведите точку T:\n"))
    Yt= input("Ввведите последовательность Yt через запятую:\n")
    Yt=Yt.split(',')
    Yt=list(map(float,Yt))
    if Tx.is_integer():
        print("("+str(Tx)+","+str(Yt[int(Tx-1)])+")")
    else:
        print("("+str(Tx)+","+str(interpolate(Yt,Tx))+")")
elif answer=="b":
    Yt= input("Ввведите последовательность Yt через запятую:\n")
    Yt=Yt.split(',')
    Yt=list(map(float,Yt))
    lengthY=len(Yt)
    lengthY=str(lengthY)
    Tx = float(input("Ввведите время из промежутка 0-t-"+lengthY+":\n"))
    while Tx>=0:
        if Tx.is_integer():
            print("("+str(Tx)+","+str(Yt[int(Tx-1)])+")")
        else:
            print("("+str(Tx)+","+str(interpolate(Yt,Tx))+")")
        Tx = float(input("Ввведите время из промежутка 1-t-"+lengthY+":\n"))
elif answer=="c":
    Yt=[4.4,2.0,11.0,21.5,7.5]
    Tx1=2.5
    Tx2=3.1
    print("("+str(Tx1)+","+str(interpolate(Yt,Tx1))+")")
    print("("+str(Tx2)+","+str(interpolate(Yt,Tx2))+")")
else:
    print("Вы ввели не правильный номер задачи")