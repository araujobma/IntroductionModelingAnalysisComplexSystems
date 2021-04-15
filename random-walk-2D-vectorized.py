# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 18:18:06 2021

@author: bruno
"""

import pycxsimulator
from pylab import *

n = 10000 #number of particles
sd = 1 #standard dev of Gaussian Noise

def initialize():
    
    global x_array, y_array, ts
    
    ts = 0
    x_array = normal(0,1,n)
    y_array = normal(0,1,n)    
    
def observe():
    
    global x_array, y_array
    
    cla()
    plot(x_array, y_array, '.',color='green')
    axis('scaled')
    axis([-100, 100, -100, 100])
    title('t = ' + str(ts))

def update():
    
    global x_array, y_array, ts
            
    ts += 1

    x_array += normal(0,sd,n)
    y_array += normal(0,sd,n)
    
    
pycxsimulator.GUI().start(func=[initialize, observe, update])