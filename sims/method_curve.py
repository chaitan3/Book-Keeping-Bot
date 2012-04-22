from pylab import *
from sim import simulate
from curve import curvature

l = 10.0

#Destination
dests = array(curvature(10))

#initial point
initial = [0.0, 0.0]

#stud mag without grid
[x, y, gx, gy, corr, err] = simulate(0, l, initial, pi/2, dests, 1.0, c_mag = 1e-2,c_align=0)
print err
plot(x,y, 'black', label='High resolution Sensor')

#hagga mag without grid
[x, y, gx, gy, corr, err] = simulate(0, l, initial, pi/2, dests, 1.0, c_mag = 1.5e-1,c_align=0)
print err
plot(x,y, 'black', label='Low resolution sensor', linestyle='-.')

#hagga mag with grid
[x, y, gx, gy, corr, err] = simulate(10, l, initial, pi/2, dests, 1.0, c_mag = 1.5e-1,c_align=0)
print err
plot(x,y, 'gray',label='Low resolution sensor with Grid')

legend(loc=4)

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
plot(destx, desty,label='Desired path', linestyle='--')
xlabel('x(m)')
ylabel('y(m)')
axis('image')
show()
