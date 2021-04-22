# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 23:59:55 2021

@author: bruno
"""
import pycxsimulator
from pylab import *

n = 3000 # size of space: n x n
p = 0.20 # probability of initially panicky individuals


def set_panicky(indice):
    global config, nextconfig, ind
    count = 0
    
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            count += config[(indice[0] + dx) % n, (indice[1] + dy) % n]
    
    if count >= 4:
        nextconfig[indice[0]][indice[1]] = 1
    
    else:
        nextconfig[indice[0]][indice[1]] = 0

set_panickyv = vectorize(set_panicky)


def initialize():
    
    global config, nextconfig,ids
    config = (random((n,n)) < p) * 1
    nextconfig = zeros((n,n))
    
    # create array with the config array indices as tuple (x,y)
    ids = indices((n,n))
    ids = array(list(zip(ids[0].ravel(),ids[1].ravel())), dtype='i,i')
    
    
def observe():
    global config, nextconfig
    cla()
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)


def update():
    
    global config, nextconfig, ids
    
    set_panickyv(ids)
    config, nextconfig = nextconfig, config
    

#pycxsimulator.GUI().start(func=[initialize, observe, update])
    
import time
init_time = 0
end_time = 0

init_time = time.time()
initialize()

for t in range(5):
    
    print("iteration ", t+1)
    update()
    observe()
    
end_time = time.time()

print(end_time - init_time)
