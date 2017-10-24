'''
GoldenSectionSearchAlgorithm
Date:   10/13/17
Class:  ME441_EngineeringOptimization
Author: Xiaoyi Liu
'''
import numpy as np

cG=(-1+np.sqrt(5))/2
#cG=0.618
#print("cG=",cG)
delta=0.05

#def fLinear(x):
#    return  7*x*x-20*x+22

#def fLinear(x):
#    return  7*x*x-20*x+22

def InitialBracketing(fLinear):
    xl=-10
    xm=xl+delta
    xu=xm+(1+cG)*delta
    while((fLinear(xl)-fLinear(xm))
            *(fLinear(xm)-fLinear(xu))>0):
        xl=xm
        xm=xu
        xu=xm+(1+cG)*(xm-xl)
    return(xl,xu)

def GoldenSection(fLinear,a,b):
    (a,b)=(InitialBracketing(fLinear))
    c=a+(1-cG)*(b-a)
    d=a+cG*(b-a)
    fc=fLinear(c)
    fd=fLinear(d)

    while((np.abs(a-b))>0.001):
#        print("a=",a,"b=",b,"fc=",fc,"fd=",fd)
        if(fc<fd):
            b=d
            d=c
            c=a+(1-cG)*(b-a)
            fd=fc
            fc=fLinear(c)
        else:
            a=c
            c=d
            d=a+cG*(b-a)
            fc=fd
            fd=fLinear(d)
#    print(a,b)
    return np.array([fLinear((a+b)/2),(a+b)/2])

#(a,b)=(InitialBracketing(fLinear))
#print(InitialBracketing())
#print(GoldenSection(fLinear,a,b))
