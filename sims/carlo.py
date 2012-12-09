from pylab import *
import sim, monte

l = 10.0

#Destination
dests = []
for i in arange(0.1*l, 1.1*l, 0.1*l):
	dests.append([i,i])
dests = array(dests)

#initial point
initial = [0.0, 0.0]
err_range = arange(0, 0.11, 0.01)
print err_range

errs = []
for i in err_range:
  [x, y, gx, gy, corr, err] = sim.simulate(9, l, initial, pi/2, dests, 1.0,1,100, c_slip=i)
  errs.append(err)
print errs

errs = []
for i in err_range:
  [x, y, gx, gy, corr, err] = sim.simulate(9, l, initial, pi/2, dests, 1.0,1,100, c_mag=i)
  errs.append(err)
print errs

mesh = []
errs = []
for i in err_range:
  for j in err_range:
    mesh.append([i, j])
    [x, y, gx, gy, corr, err] = monte.simulate(9, l, initial, pi/2, dests, 1.0,1,100, c_slip=i, c_mag=j)
    errs.append(err)
print mesh
print errs
