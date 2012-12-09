from pylab import *
from sim import simulate

l = 0.2

#Destination
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
#initial point
initial = [0.0, 0.0]

#actual plot1
[x, y, gx, gy, corr, err] = simulate(0, l, initial, pi/2, dests, 1.0, 1, 100)
print err
plot(array(x)*10,array(y)*10, 'black', label='0 correction', linewidth=2)
#actual plot2
[x, y, gx, gy, corr, err] = simulate(1, l, initial, pi/2, dests, 1.0, 1, 100)
print err
plot(array(x)*10,array(y)*10, 'green', label='1 correction', linewidth=2)
#actual plot3
[x, y, gx, gy, corr, err] = simulate(2, l, initial, pi/2, dests, 1.0, 1, 100)
print err
plot(array(x)*10,array(y)*10, 'blue', label='2 corrections', linewidth=2)
legend(loc=2)

l *= 10
dests *= 10
gx *= 10
gy *= 10

for i in gx:
  plot([i,i], [0,l], 'red')
for i in gy:
  plot([0,l], [i,i], 'red')
destx = [initial[0]]
desty = [initial[1]]
for i in dests:
  destx.append(i[0])
  desty.append(i[1])
  
  
plot(destx, desty,label='Desired path', linestyle='--', linewidth=2)
xlabel('x coordinate position, x(m)')
ylabel('y coordinate position, y(m)')
axis('image')
axis([0, l, 0, l])
show()

