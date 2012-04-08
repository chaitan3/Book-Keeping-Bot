from pylab import *
from sim import simulate

l = 10.0

#Destination
dests = array([
[l,l]
])

#initial point
initial = [0.0, 0.0]

[x, y, gx, gy, err] = simulate(10, l, initial, pi/2, dests, 1.0)

print err
  
plot(x,y, label='Actual Path')
axis([0, l, 0, l])
for i in gx:
  plot([i,i], [0,l], 'red')
for i in gy:
  plot([0,l], [i,i], 'red')
destx = [initial[0]]
desty = [initial[1]]
for i in dests:
  destx.append(i[0])
  desty.append(i[1])
plot(destx, desty, 'g--',label='Desired path')
legend(loc=2)
show()
