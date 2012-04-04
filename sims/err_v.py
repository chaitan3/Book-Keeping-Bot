from pylab import *
from sim import simulate
v = []
errors = []
initial = [0.0,0.0]
dests = array([[1.0, 1.0]])
for n in arange(0.1, 0.5, 0.1):
  errs = []

  for j in range(0,10):
    print n, j
    tmp = simulate(10, initial, dests, n)
    errs.append(tmp[-1])
    
  v.append(n)
  errors.append(average(errs))  
  print n, errors[-1]
plot(v, errors)
show()



