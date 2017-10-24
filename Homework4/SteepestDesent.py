'''
SteepestDescentAlgorithm
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
df0=dfQuar(x0)
epsilon=0.001
i=0
while (np.linalg.norm(df0)>epsilon):
    print('Step # = ',i)
    dr=-df0
    def localf(alpha):
        return fQuar(x0+alpha*dr)
    [ff,alpha0]=GoldenSection(localf,-1,1)
    print('df= ', df0, 'x= ', x0,'alpha= ',alpha0, 'f0= ',f0,'norm= ',np.linalg.norm(df0))
    x0=x0+alpha0*dr
    f0=fQuar(x0)
#    df00=df0
    df0=dfQuar(x0)
#    print(np.dot(df00,df0))
    i=i+1;
