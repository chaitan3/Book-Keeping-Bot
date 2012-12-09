from pylab import *
from sim import simulate
from curve import curvature

l = 10

dests = array(curvature(10))

#initial point
initial = [0.0, 0.0]

[x, y, gx, gy, corr, err] = simulate(9, l, initial, pi/2, dests, 1.0, 1.0,100,c_slip=0.21, c_mag=0.1, c_align=0.1037);

print err
print corr
  
plot(x,y,label='Actual path', linewidth=2)
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
#xlabel('x coordinate position, x(m)')
#ylabel('y coordinate position, y(m)')
axis('image')
#legend(loc=2)
show()

