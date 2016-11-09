# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:36:40 2016

@author: Никита
"""
import numpy as np
x=np.linspace(0,10,10,False,False,None)
z=np.zeros(4)
z[0]=np.random.choice(x)
z[1]=np.random.choice(x)
z[2]=np.random.choice(x)
z[3]=np.random.choice(x)

print(z)