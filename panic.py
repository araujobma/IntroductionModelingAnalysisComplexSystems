# -*- coding: utf-8 -*-


import pycxsimulator
from pylab import *

n = 3000 # size of space: n x n
p = 0.20 # probability of initially panicky individuals

def initialize():
    global config, nextconfig
    config = zeros([n, n])
    for x in range(n):
        for y in range(n):
            config[x, y] = 1 if random() < p else 0
    nextconfig = zeros([n, n])
    
def observe():
    global config, nextconfig
    cla()
    imshow(config, vmin = 0, vmax = 1, cmap = cm.binary)

def update():
    global config, nextconfig
    for x in range(n):
        for y in range(n):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    count += config[(x + dx) % n, (y + dy) % n]
            nextconfig[x, y] = 1 if count >= 4 else 0
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