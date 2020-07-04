# define the steps of simulation using vectorized operations(multiplication)
from pylab import *
import numpy as np
import math

def apply_trf_funcs(x, trf_funcs):
	
	x_vec_trfmd = []
	for i, func in enumerate(trf_funcs):
		#print(x_vec)
		x_vec_trfmd.append( list(map(func,[x]))[0] )
	return x_vec_trfmd

def initialize(x0_vec):
    global x, result
    x = x0_vec
    result = [x0_vec]
	
	
def observe():
    global x, result
    result.append(x)
	
	
def update(A_vec, trf_funcs=[]):
    global x, result
	if trf_funcs == []:
		x = np.matmul(A,x)
	else:
		x_new = []
		for i, func in enumerate(trf_funcs):
			x_new.append(func(x))
		x = x_new
	
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
	

#-----------------------logistic growth model eq. 4.26 ---------------------------
# equatiion in the form (1+r)*x - (r/k)*x^2

# r = percentage of growth, k = max population desired(carrying capacity of the environment)

r = 0.20
k = 1000000
A = np.array([(1+r),-r/k])
x0 = 1000 # initial population(x)

trf_funcs = [lambda x: x*1, lambda x: math.pow(x,2)]

initialize(x0)

for t in range(40):
    update(A, trf_funcs)
    observe()
	
result = np.array(result)

plot(result)



#-----------------------predator prey interactions Lotka-Volterra models eqs. 4.34 and 4.35---------------------------
# equation for prey in the form ( (1+r) - (1-(1/(b*y+1))) )*x - (r/k)*x^2
# equation for predator in the form (1-d)*y + c*x*y

# r = growth rate of prey, k = max population desired(carrying capacity of the environment) of prey
# d = death rate of predator c = how fast prdators increases as preys increase
# b = how fast preys decrease as predators increase

r = 1
k = 100
c = 1
d = 1
b = 1
A = [] #np.array([(1+r) - (1-(1/(b*y+1))), -(r/k)], [1-d, c])
x0 = [8,1] # initial population([x,y])

trf_funcs = [lambda x: ( (1+r) - (1-(1/(b*x[1]+1))) )*x[0] - (r/k)*math.pow(x[0],2),\
			 lambda x: (1-d)*x[1] + c*x[0]*x[1]]


initialize(x0)

for t in range(50):
    update(A, trf_funcs)
    observe()
	
result = np.array(result)

plot(result)
plot(result[:,0], result[:,1])