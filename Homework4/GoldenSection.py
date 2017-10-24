'''
GoldenSectionSearchAlgorithm
Date:   10/13/17
Class:  ME441_EngineeringOptimization
Author: Xiaoyi Liu
'''
import numpy as np

cG=(-1+np.sqrt(5))/2
#cG=0.618
print("cG=",cG)
delta=0.05

def fLinear(x):
    return  7*x*x-20*x+22

#def fLinear(x):
#    return  7*x*x-20*x+22

def InitialBracketing(fLinear):
    xl=0
    xm=xl+delta
    xu=xm+(1+cG)*delta
    while((fLinear(xl)-fLinear(xm))
            *(fLinear(xm)-fLinear(xu))>0):
        xl=xm
        xm=xu
        xu=xm+(1+cG)*(xm-xl)
    return(xl,xu)

def GoldenSection(fLinear,a,b):
#    (a,b)=(InitialBracketing(fLinear))
    c=a+(1-cG)*(b-a)
    d=a+cG*(b-a)
    fa=fLinear(a)
    fb=fLinear(b)
    fc=fLinear(c)
    fd=fLinear(d)
    i=0
    print('Step#: ', i, 'a             b             c             d             fa             fb             fc             fd\n')

    while((np.abs(a-b))>0.001):
        if(fc<fd):
            b=d
            fb=fd
            d=c
            fd=fc
            c=a+(1-cG)*(b-a)
            fc=fLinear(c)
        else:
            a=c
            fa=fc
            c=d
            fc=fd
            d=a+cG*(b-a)
            fd=fLinear(d)
        i+=1
        print('Step#: ', i, a,  b, c, d, fa, fb,fc,fd,'\n')
#    print(a,b)
    return np.array([fLinear((a+b)/2),(a+b)/2])

(a,b)=(InitialBracketing(fLinear))
#print(InitialBracketing())
print('Optimal Solution: ', GoldenSection(fLinear,a,b))
