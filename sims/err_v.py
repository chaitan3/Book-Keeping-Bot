from pylab import *
from sim import simulate
v = []
avg_errors = []
max_errors = []
initial = [0.0,0.0]
l = 10.0
dests = array([
[l/5,l/5],
[2*l/5,2*l/5],
[3*l/5,3*l/5],
[4*l/5,4*l/5],
[l,l]
])
for n in arange(1.0, 5.5,0.5):
  errs = []
  
  for j in range(0,100):
    print n, j
    tmp = simulate(10, l, initial, pi/2, dests, n)
    errs.append(tmp[-1])
    
  v.append(n)
  avg_errors.append(average(errs))  
  max_errors.append(max(errs))
  
  print n, avg_errors[-1], max_errors[-1]
print v
print avg_errors
print max_errors


