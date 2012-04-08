from pylab import *
l = 10.0
dests = []
for x in arange(0.0, l, 0.1):
  y = (x*(2*l - x))**0.5
  dests.append([x, y])
print dests
