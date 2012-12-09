from pylab import *
from sim import simulate
from curve import curvature
p = []
avg_errors = []
max_errors = []
initial = [0.0,0.0]
l = 10.0
#dests = array([
#[l/5,l/5],
#[2*l/5,2*l/5],
#[3*l/5,3*l/5],
#[4*l/5,4*l/5],
#[l,l]
#])
dests = []
for i in arange(0.1*l, 1.1*l, 0.1*l):
	dests.append([i,i])
dests = array(dests)
#dests = array(curvature(10))

for b in range(1, 11):
  errs = []
  
  for j in range(0,100):
    print b, j
    tmp = simulate(9, l, initial, pi/2, dests, 1.0,b,100)
    errs.append(tmp[-1])
    
  p.append(b)
  avg_errors.append(average(errs))  
  max_errors.append(max(errs))
  
  print b, avg_errors[-1], max_errors[-1]
print p
print avg_errors
print max_errors


