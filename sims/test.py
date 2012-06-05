from pylab import *
from sim import simulate

l = 10.0

#Destination
dests = []
for i in arange(0.1*l, 1.1*l, 0.1*l):
	dests.append([i,i])
dests = array(dests)

#initial point
initial = [0.0, 0.0]

[x, y, gx, gy, corr, err] = simulate(10, l, initial, pi/2, dests, 1)

print err
print corr
  
plot(x,y, label='Actual Path',linewidth=2)
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
plot(destx, desty, 'g--',label='Desired path', linewidth=2)
xlabel('x coordinate position, x(m)')
ylabel('y coordinate position, y(m)')
axis('image')
legend(loc=2)
show()
