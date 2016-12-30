# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 23:51:34 2016

@author: Никита
"""
from numpy import sin,pi,linspace,sqrt,zeros
from matplotlib import pyplot
def sinesum(t,b):
    if(t==[]):
        S=zeros(len(t))
        for j in range(len(t)):
            for i in range(len(b)):
                S[j]+=b[i]*sin((i+1)*t[j])
    else:
        S=0.
        for i in range(len(b)):
                S+=b[i]*sin((i+1)*t)
    return S

def test_sinesum():
    t=[-pi/2,pi/2]
    b=[4,-3]
    print("Результат функции sinesum:")
    print(sinesum(t,b))
    S=[0.,0.]
    S[0]=4.*sin((-pi)/2)+4*sin(2*pi/2)
    S[1]=-3.*sin((-pi)/2)-3*sin(2*pi/2)
    print("Вручную:")
    print(S)

def plot_compare(f,N,M,b):
    t=linspace(-pi,pi,M)
    S=sinesum(t,b)
    y=f(t)
    pyplot.xlabel("t")
    pyplot.plot(S,t)
    pyplot.plot(y,t)
    pyplot.show()
    
def error(b,f,M):
    t=linspace(-pi,pi,M)
    E=0.
    Sn=sinesum(t,b)
    for i in range(M):
        E+=(f(t[i])-Sn[i])**2
    E=sqrt(E)
    return E

def trial(f,N):
    flag=1
    while(flag==1):
        b_str=input("Введите b через запятую:\n")
        b=[float(s) for s in b_str.split(',')]
        plot_compare(f,N,500,b)
        print("Погрешность:")
        print(error(b,f,500))
        flag=int(input('''Если вас устраивает погрешность введите 0
                       иначе введите 1:\n'''))
def f(t):
    return t/pi

b1=-2.
b2=-2.
b3=-2.
B1=linspace(-1,1,20)
B2=linspace(-1,1,20)
B3=linspace(-1,1,20)
err=10000.
b=[0,0,0]
err_vrem=10000.
for i in range(20):
    for j in range(20):
        for k in range(20):
           b[0]=B1[i]
           b[1]=B2[j]
           b[2]=B3[k]
           err_vrem=error(b,f,500)
           if err_vrem<err:
               err=err_vrem
               b1=B1[i]
               b2=B2[j]
               b3=B3[k]
plot_compare(f,3,3,b)
print("Коофициенты:")
print(b)
print("Погрешность:")
print(err)
