from pylab import *
from sim import simulate

#Destination
dests = array([
[0.25, 0.65],
[0.85,0.15],
[1.0, 1.0]
])

#initial point
initial = [0.0, 0.0]

[x, y, gx, gy, err] = simulate(5, initial, dests, 0.5)

print err
  
plot(x,y)
axis([0, 1, 0, 1])
for i in gx:
  plot([i,i], [0,1], 'red')
for i in gy:
  plot([0,1], [i,i], 'red')
destx = [initial[0]]
desty = [initial[1]]
for i in dests:
  destx.append(i[0])
  desty.append(i[1])
plot(destx, desty)
show()
