from pylab import *
from sim import simulate
v = []
errors = []
initial = [0.0,0.0]
l = 10.0
dests = array([[l, l]])
for n in arange(1.0, 2.0, 0.2):
  errs = []

  for j in range(0,10):
    print n, j
    tmp = simulate(10, l, initial, dests, n)
    errs.append(tmp[-1])
    
  v.append(n)
  errors.append(average(errs))  
  print n, errors[-1]
print v
print errors


