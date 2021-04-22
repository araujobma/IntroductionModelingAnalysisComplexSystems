# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 23:59:55 2021

@author: bruno
"""
import pycxsimulator
from pylab import *
import time
from numba import jit

n = 10000 # size of space: n x n
p = 0.25 # probability of initially panicky individuals

@jit(nopython=True)
def new_config(ids,counts,config):
    
    
        
    #for every indice(x,y) counts neighbors
    for indice in ids:
        
        counts[indice[0],indice[1]] = \
        \
        config[(indice[0]-1) % n, (indice[1]-1) % n] + \
        config[(indice[0]-1) % n, (indice[1]) % n] + \
        config[(indice[0]-1) % n, (indice[1]+1) % n] + \
        config[(indice[0]) % n, (indice[1]-1) % n] + \
        config[(indice[0]) % n, (indice[1]) % n] + \
        config[(indice[0]) % n, (indice[1]+1) % n] + \
        config[(indice[0]+1) % n, (indice[1]-1) % n] + \
        config[(indice[0]+1) % n, (indice[1]) % n] + \
        config[(indice[0]+1) % n, (indice[1]+1) % n]
    
    
    return (counts >= 4) * 1




def initialize():
    seed(0)
    
    global config, ids, counts
    config = (random((n,n)) < p) * 1
    counts = zeros((n,n))
    
    # create array with the config array indices as array [ [x1,y1], [x1,y2], ..., [xn,yn] ]
    ids = indices((n,n))
    ids = np.dstack((ids[0].ravel(),ids[1].ravel()))[0]
    
    
def observe():
    global config
    cla()
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)


def update():
    
    
    global config, counts,ids
    
    
    config = new_config(ids,counts,config)
    

        
    

#pycxsimulator.GUI().start(func=[initialize, observe, update])
    

init_time = 0
end_time = 0

init_time = time.time()
initialize()

for t in range(5):
    
    print("iteration ", t+1)
    update()
    #observe()
    
end_time = time.time()

print(end_time - init_time)
