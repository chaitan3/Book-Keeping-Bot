from pylab import *
from sim import simulate
from curve import curvature
v = []
avg_errors = []
max_errors = []
initial = [0.0,0.0]
l = 10.0
#dests=array(curvature(10))
dests = []
for i in arange(0.1*l, 1.1*l, 0.1*l):
	dests.append([i,i])
dests = array(dests)
for n in arange(1.0, 5.5,0.5):
  errs = []
  for j in range(0,10):
    print n, j
    tmp = simulate(9, l, initial, pi/2, dests, n,1,100)
    errs.append(tmp[-1])
    
  v.append(n)
  avg_errors.append(average(errs))  
  max_errors.append(max(errs))
  
  print n, avg_errors[-1], max_errors[-1]
print v
print avg_errors
print max_errors


