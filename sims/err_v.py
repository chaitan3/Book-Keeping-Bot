from pylab import *
from sim import simulate
v = []
avg_errors = []
max_errors = []
initial = [0.0,0.0]
l = 10.0
dests = array([[l, l]])
for n in arange(1.0, 2.1,0.1):
  errs = []
  
  for j in range(0,10):
    print n, j
    tmp = simulate(10, l, initial, pi/2, dests, v)
    errs.append(tmp[-1])
    
  v.append(n)
  avg_errors.append(average(errs))  
  max_errors.append(max(errs))
  
  print n, avg_errors[-1], max_errors[-1]
print v
print avg_errors
print max_errors


