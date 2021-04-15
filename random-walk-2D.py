# -*- coding: utf-8 -*-


import pycxsimulator
from pylab import *

n = 10 #number of particles
sd = 3 #standard dev of Gaussian Noise

def initialize():
    global xlist, ylist, time
    
    time = 0
    xlist, ylist = [],[]
    
    for i in range(n):
        xlist.append(normal(0,1))
        ylist.append(normal(0,1))

def observe():
    global xlist, ylist
    cla()
    plot(xlist[0:5], ylist[0:5], '.',color='green')
    plot(xlist[5:10], ylist[5:10], '.',color='blue')
    axis('scaled')
    axis([-100, 100, -100, 100])
    title('t = ' + str(time))
    
    
def update():
    global xlist, ylist, time
            
    time += 1

    for i in range(n):
        xlist[i] += normal(0, sd)
        ylist[i] += normal(0, sd)

pycxsimulator.GUI().start(func=[initialize, observe, update])
