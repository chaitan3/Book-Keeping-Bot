from pylab import *
def curvature(r):
  l = 10.0
  dests = []
  a = (l/2)+((2*(r**2)-l**2)**0.5)/2
  z = arange(0.0,11.0)
  for i in z:
    x = a-r*cos(arctan2(-a,-l+a)+((10-i)/10)*(-arctan2(-a,-l+a)+arctan2(l-a,a)))
    y = l-a-r*sin(arctan2(-a,-l+a)+((10-i)/10)*(-arctan2(-a,-l+a)+arctan2(l-a,a)))
    
    dests.append([x, y])
  return dests
