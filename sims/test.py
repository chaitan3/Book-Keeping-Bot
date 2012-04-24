from pylab import *
from sim import simulate

l = 10.0

#Destination
dests = array([
[l/5,l/5],
[2*l/5,2*l/5],
[3*l/5,3*l/5],
[4*l/5,4*l/5],
[l,l]
])

#initial point
initial = [0.0, 0.0]

[x, y, gx, gy, corr, err] = simulate(10, l, initial, pi/2, dests, 1.0)

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
