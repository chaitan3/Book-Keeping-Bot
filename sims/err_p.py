from pylab import *
from sim import simulate
p = []
errors = []
initial = [0.0,0.0]
dests = array([[1.0, 1.0]])
for n in range(1, 11):
  errs = []

  for j in range(0,10):
    print n, j
    tmp = simulate(n, initial, dests, 0.1)
    errs.append(tmp[-1])
    
  p.append(n)
  errors.append(average(errs))  
  print n, errors[-1]
plot(p, errors)
show()


