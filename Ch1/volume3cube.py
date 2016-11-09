# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:30:35 2016

@author: Никита
"""

import numpy as np
import matplotlib.pyplot as plt

L = np.linspace(1,3,num=3)
V0=L[0]**3
V1=L[1]**3
V2=L[2]**3
V=L**3
plt.plot(L,V)
print("Результаты V=L**3 ="+str(V))
print("Результаты счета вручную")
print("V0 = "+str(V0))
print("V1 = "+str(V1))
print("V2 = "+str(V2))