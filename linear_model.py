# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:40:31 2021

@author: bruno
"""

# define the steps of simulation using vectorized operations(multiplication)
from pylab import *
import pycxsimulator

def apply_trf_funcs(x, trf_funcs):
	
	x_vec_trfmd = []
	for i, func in enumerate(trf_funcs):
		#print(x_vec)
		x_vec_trfmd.append( list(map(func,[x]))[0] )
	return x_vec_trfmd

def initialize():
    global x, result
    x = array([1,1])
    result = [x]
	
	
def observe():
    global x, result
    result.append(x)
    
    plot(result)
	
	
def update():
    
    trf_funcs=[]
    #Eq. 4.17 on book
    A = array([ [0.5,1],[-0.5,1] ])
    
    global x, result
    if trf_funcs == []:
        x = matmul(A,x)
    else:
        x_new = []
        for i, func in enumerate(trf_funcs):
            x_new.append(func(x))
        x = x_new
	
   
#-------------------------------------------------------

pycxsimulator.GUI().start(func=[initialize, observe, update])

