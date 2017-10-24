'''
Fletcher-Reeves Conjugate Gradient Algorithm
Date:   10/13/17
Class:  ME441_EngineeringOptimization
Author: Xiaoyi Liu
'''
import numpy as np
#import matplotlib.pyplot as plt
from GoldenSection_For_Multiopt import GoldenSection

def fQuar(x):
    return x[0]**2+2*x[1]**2+2*x[2]**2 + 2*x[0]*x[1]+2*x[1]*x[2]

def dfQuar(x):
    return np.array([2*x[0]+2*x[1], 2*x[0]+4*x[1]+2*x[2], 2*x[1]+4*x[2]])

#SteepestDescentAlgorithm
x0=[1,1,1]
f0=fQuar(x0)
c0=dfQuar(x0)
c1=c0
d0=-c0
d1=d0
epsilon=0.001
i=0
while (np.linalg.norm(d1)>epsilon and i<10):
    print('Step # = ',i)
    def localf(alpha):
        return fQuar(x0+alpha*d1)
    [ff,alpha0]=GoldenSection(localf,-1,1)
    print('df= ', d1, 'x= ', x0,'alpha= ',alpha0, 'f0= ',f0,'norm= ',np.linalg.norm(d0))
    x0=x0+alpha0*d1
    f0=fQuar(x0)
    c0=c1
    c1=dfQuar(x0)
    d0=d1
    d1=-c1+d0*((np.linalg.norm(c1)/np.linalg.norm(c0))**2)
    print('c0= ',c0,'beta=',(np.linalg.norm(c1)/np.linalg.norm(c0))**2,'c1=',c1)
    print(d1)
    i=i+1;
