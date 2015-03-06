# -*- coding: utf-8 -*-
"""
Assignment 6 problem 1
Simlulates the radioactive decay of 10 000 atoms
of 213 Bi. Returns a plot of the numbers of 213 Bi, 
209 Tl, 209 Pb, and 209 Bi atoms as a function of time
for 20 000 seconds.
"""
from random import random
from numpy import arange
from pylab import plot, xlabel, ylabel, show, legend
# Constants
NBi_1=10000         # number of 213 Bi atoms
NBi_2=0             # number of 209 Bi atoms
NTl=0               # number of 209 Tl atoms
NPb=0               # number of 209 Pb atoms
tau_Bi=46.0*60      # half-life of 213 Bi
tau_Tl=2.2*60       # half-life of 209 Tl
tau_Pb=3.3*60       # half-life of 209 Pb
h = 1.0             # step size in seconds
p_Bi=1.0-2.0**(-h/tau_Bi)       # prob. of decay of 213 Bi in one step
p_Tl=1.0-2.0**(-h/tau_Tl)       # prob. of decay of 209 Tl in one step
p_Pb=1.0-2.0**(-h/tau_Pb)       # prob. of decay of 209 Pb in one step
tmax=20000          # total time in seconds
# Lists of plot points
tpoints=arange(0.0,tmax,h)
Bi_1points=[]
Bi_2points=[]
Tlpoints=[]
Pbpoints=[]

for t in tpoints:
    Bi_1points.append(NBi_1)
    Bi_2points.append(NBi_2)
    Tlpoints.append(NTl)
    Pbpoints.append(NPb)
    decay_Pb=0
    for i in range(NPb):        # calc. number of 209 Pb atoms
        if random()<p_Pb:       # which decay
            decay_Pb+=1
    NPb-=decay_Pb               # subtracts this from 209 Pb
    NBi_2+=decay_Pb             # adds to 209 Bi
    decay_Tl=0
    for j in range(NTl):        # same for 209 Tl
        if random()<p_Tl:
            decay_Tl+=1
    NTl-=decay_Tl               # subtracts this from 209 Tl
    NPb+=decay_Tl               # adds to 209 Pb
    decay_Bi_route1=0           # number of atoms which decay to 209 Pb
    decay_Bi_route2=0           # number of atoms which decay to 209 Tl
    for k in range(NBi_1):
        if random()<p_Bi:       # probability of 213 Bi decaying to 'something'
            if random()-.9791<1.0e-9:          # uses prob. .9791 within 1.0e-9 precision
                decay_Bi_route1+=1      # of 213 Bi decaying to 209 Pb
            else:                       # if not, then must decay to 209 Tl
                decay_Bi_route2+=1      # (prob. is .0209)
    NBi_1-=decay_Bi_route1      # subtracts number of Bi decaying to Pb
    NBi_1-=decay_Bi_route2      # subtracts number of Bi decaying to Tl
    NPb+=decay_Bi_route1        # and adds to number of Pb
    NTl+=decay_Bi_route2        # and adds to number of Tl

plot(tpoints,Bi_1points,label="213 Bi")
plot(tpoints,Bi_2points,label="209 Bi")
plot(tpoints,Tlpoints,label="209 Tl")
plot(tpoints,Pbpoints,label="209 Pb")
xlabel("Time")
ylabel("Number of Atoms")
legend()
show()
