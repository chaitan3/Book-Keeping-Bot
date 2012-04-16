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

#stud mag without grid
[x, y, gx, gy, err] = simulate(0, l, initial, pi/2, dests, 1.0, c_mag = 1e-2,c_align=0)
print err
plot(x,y, 'black', label='Good Sensor')

#hagga mag without grid
[x, y, gx, gy, err] = simulate(0, l, initial, pi/2, dests, 1.0, c_mag = 1.5e-1,c_align=0)
print err
plot(x,y, 'black', label='Bad sensor', linestyle='-.')

#hagga mag with grid
[x, y, gx, gy, err] = simulate(10, l, initial, pi/2, dests, 1.0, c_mag = 1.5e-1,c_align=0)
print err
plot(x,y, 'gray',label='Bad sensor with Grid')

legend(loc=2)

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

