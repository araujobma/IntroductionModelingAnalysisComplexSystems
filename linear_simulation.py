# define the steps of simulation using vectorized operations(multiplication)
from pylab import *
import numpy as np

def initialize(x0_vec):
    global x, result
    x = x0_vec
    result = [x0_vec]
	
	
def observe():
    global x, result
    result.append(x)
	
	
def update(A_vec):
    global x, result
	x = np.matmul(A,x)
	
#-------------------------------------------------------


# simulate and plot equation 4.17 ----------------------
A = np.array([ [0.5,1],[-0.5,1] ])
x0 = np.array([1,1])

initialize(x0)

for t in range(30):
    update(A)
    observe()
	
result = np.array(result)

plot(result)

plot(result[:,0], result[:,1])
#---------------------------------------------------------------------



# exercise 4.7 -------------------------------------------------

#plot for timesteps
np.random.seed(13)
for k in range(10):
	A = np.random.uniform(-1,1,(2,2))
	initialize(x0)
	for t in range(30):
		update(A)
		observe()
	result = np.array(result)
   
	plot(result)
	input('Press enter to continue...')
	close()
	
	
#plot in the phase space
np.random.seed(13)
for k in range(10):
	A = np.random.uniform(-1,1,(2,2))
	initialize(x0)
	for t in range(30):
		update(A)
		observe()
	result = np.array(result)
   
	plot(result[:,0],result[:,1])
	input('Press enter to continue...')
	close()
#----------------------------------------------------------------------------------------	
	