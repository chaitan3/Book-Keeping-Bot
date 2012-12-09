from pylab import *
from sim import simulate
a = []
avg_errors = []
max_errors = []
initial = [0.0,0.0]
l = 10.0

for n in arange(0, (pi/2)+0.05,pi/20):
  errs = []
  dests = array([[l*cos(n), l*sin(n)]])
  
  for j in range(0,10):
    print n, j
    tmp = simulate(10, l, initial, pi/2, dests, 1.0)
    errs.append(tmp[-1])
    
  a.append(n)
  avg_errors.append(average(errs))  
  max_errors.append(max(errs))
  
  print n, avg_errors[-1], max_errors[-1]
print a
print avg_errors
print max_errors



