# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:51:05 2016

@author: Никита
"""

def mostLeft_Right(x,y):
    leftMostInd_X=0;
    rightMostInd_X=0;
    rightMost_X=x[0]
    leftMost_Y=y[0];
    leftMost_X=x[0]
    for i in range(0,len(x),1):
        if x[i] < leftMost_X:
            leftMostInd_X = i
            leftMost_X=x[i]
        elif x[i] > rightMost_X:
            rightMostInd_X = i
            rightMost_X=x[i]
        elif y[i] < leftMost_Y:
            leftMost_Y = y[i]
    if leftMost_Y < 0:
        for i in range(0,len(x),1):
            y[i] += leftMost_Y
    if leftMost_X < 0:
        for i in range(0,len(x),1):
            x[i] += leftMost_X
    return leftMostInd_X,rightMostInd_X

def squareTrapeze(x,y,leftMostInd_X,rightMostInd_X):
    i=leftMostInd_X
    S=0
    l=len(x)
    while i != rightMostInd_X:
        if (i+1) < l:
            h = abs(x[i+1]-x[i])
            S+=0.5*h*(y[i]+y[i+1])
            i=i+1
        else:
            h = abs(x[0]-x[i])
            S+=0.5*h*(y[i]+y[0])
            i=0
    print(S)
    return S

def polyarea(x,y):
    leftMostInd_X,rightMostInd_X = mostLeft_Right(x,y)
    S = squareTrapeze(x,y,leftMostInd_X,rightMostInd_X)-squareTrapeze(x,y,rightMostInd_X,leftMostInd_X)
    return S   
    
x=[1,1,4,7,7]
y=[1,4,1,4,1]
print(polyarea(x,y))