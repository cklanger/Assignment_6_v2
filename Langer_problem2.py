# -*- coding: utf-8 -*-
"""
Assignment 6 problem 2
Computes the value of the integral
I=\int_0^1 x^{-1/2}/{e^x+1} dx using Monte Carlo
integration with weight w(x)=x^{-1/2}
and probability density p(x)=1/(2\sqrt(x))
so that the transformation formula is x=z^2.
We use 1 000 000 random points.
"""
from math import sqrt,exp
from random import random

def f(x):
    return 1.0/(sqrt(x)*(exp(x)+1))
def w(x):
    return 1.0/(sqrt(x))

N=1000000
sum=0.0
for i in range(N):
    x=(random())**2.0
    sum+=f(x)/w(x)
print("The value of the integral is approximately {}".format(2*sum/N))

#########################################
# OUTPUT OF PROGRAM
# The value of the integral is approximately 
# 0.8388178370144185
