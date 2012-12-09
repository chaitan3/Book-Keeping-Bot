from pylab import *
from sim import simulate
from curve import curvature
p = []
avg_errors = []
max_errors = []
corrs = []
initial = [0.0,0.0]
l = 10.0

for n in arange(l, l*10, 3):
  errs = []
  dests=array(curvature(n))
  
  corrs.append(0)
  for j in range(0,100):
    print n, j
    tmp = simulate(9, l, initial, pi/2, dests, 1.0,1,100)
    errs.append(tmp[-1])
    corrs[-1] = tmp[-2]
    
    
  p.append(n)
  avg_errors.append(average(errs))  
  max_errors.append(max(errs))

  print n, avg_errors[-1], max_errors[-1]
print p
print avg_errors
print max_errors
print corrs


