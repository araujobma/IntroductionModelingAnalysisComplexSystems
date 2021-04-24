# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:16:39 2021

@author: bruno
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 23:59:55 2021

@author: bruno
"""
import pycxsimulator
from pylab import *
import time
from numba import jit

w = 50
h = 50
init_p = 0.10 # probability of initially alive individuals

@jit(nopython=True)
def new_config(ids,counts,config):
    
    
    
    
    #for every indice(y,x) counts neighbors
    for indice in ids:
        
        counts[indice[0],indice[1]] = \
        config[(indice[0]-1) % h, (indice[1]-1) % w] + \
        config[(indice[0]-1) % h, (indice[1]) % w] + \
        config[(indice[0]-1) % h, (indice[1]+1) % w] + \
        config[(indice[0]) % h, (indice[1]-1) % w] + \
        config[(indice[0]) % h, (indice[1]) % w] + \
        config[(indice[0]) % h, (indice[1]+1) % w] + \
        config[(indice[0]+1) % h, (indice[1]-1) % w] + \
        config[(indice[0]+1) % h, (indice[1]) % w] + \
        config[(indice[0]+1) % h, (indice[1]+1) % w]
        
        if (config[indice[0],indice[1]] == 0) and \
        (counts[indice[0],indice[1]] == 3):
            config[indice[0],indice[1]] = 1
            
        elif (config[indice[0],indice[1]] == 1) and \
        ( (counts[indice[0],indice[1]] < 3) or \
        (counts[indice[0],indice[1]] > 4) ):
            config[indice[0],indice[1]] = 0    
        




def initialize():
    #seed(0)
    
    global config, ids, counts
    config = (random((h,w)) < init_p) * 1
    counts = zeros((h,w))
    
    # create array with the config array indices as array [ [x1,y1], [x1,y2], ..., [xn,yn] ]
    ids = indices((h,w))
    ids = np.dstack((ids[0].ravel(),ids[1].ravel()))[0]
    
    
def observe():
    global config
    cla()
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)


def update():
    
    
    global config, counts,ids
    
    
    new_config(ids,counts,config)
    

        
    

pycxsimulator.GUI().start(func=[initialize, observe, update])
    
'''
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
'''