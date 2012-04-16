from pylab import *
x=[1,2,3,4,5,6,7,8,9,10]
y=[1,2,3,4,5,6,7,8,9,10]

for i in x:
 plot([i,i], [0,10], 'red')
for i in y:
 plot([0,10],[i,i],'red')
xlabel('X AXIS')
ylabel('Y AXIS')
show()
