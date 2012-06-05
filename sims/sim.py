from pylab import *
from time import sleep

#sensor error modelling, bot destination check
#Error plots pitch, speed, different trajectories

def restrict_angle(a):
	if a > pi:
		return restrict_angle(a - 2*pi)
	elif a < -pi:
		return restrict_angle(a + 2*pi)
	return a

def simulate(n, l, initial, init_a, dests, v, c_slip=5e-2, c_mag=5e-2, c_align=10e-2 ):

  #Global environment coordinates
  env = array(initial)
  bot = env.copy()
  prev_dest = env.copy()
  env_a = init_a
  bot_a = init_a
  x = [initial[0]]
  y = [initial[1]]
  
  #Laser Grid
  d = l/(n+1)
  gx = arange(d, l, d)
  gy = gx.copy()
  #Laser intercept size
  di = d*1e-2
  #Laser Failure
  #gy=delete(gy,2)

  #Slippage error
  v_err = v*(c_slip)
  #Motor alignment error
  v_al = v*(c_align)

  #Sensor Angle error 
  a_err = c_mag
  
  #Distance between motor wheels
  b = 0.1

  #Time step 
  dt = 1e-2
  t = 0
  #Error
  err = 0
  #Corrections
  corr = 0

  #Path length
  path = 0.0
  
  #Control Law constants
  k1 = 1
  k2 = 100
  beta = 0.1
  gamma = 0.4

  def vert_grid():
    for i in gx:
      if i != no_x:
        if abs(env[0] - i) < di:
          return i
    return 0
    
  def horiz_grid():
    for i in gy:
      if i != no_y:
        if abs(env[1] - i) < di:
          return i
    return 0

  for index in range(0,len(dests)):
	  
    dest = dests[index]
    if index > 0:
	  prev_dest = dests[index - 1]
    if index < len(dests) - 1:
	  next_dest = dests[index + 1]
    else:
	  next_dest = 2*dests[index]-dests[index-1]
		
    no_x = 0
    no_y = 0

    path += norm(dest-prev_dest)
    
    r = 1

    while r > 0.01:
      hit = horiz_grid() 
      if hit:
        no_y = hit
        #reset y coordinate
        bot[1] = env[1]
        #Increment the number of corrections
        corr += 1
        
      hit = vert_grid()
      if hit:
        no_x = hit
        #reset x coordinate
        bot[0] = env[0]
        corr += 1
        
      #Bot reads magnetometer
      bot_a = restrict_angle(env_a + a_err*normal())
      
      #Control Law
      #Calculate delta, theta and r
      target_a = arctan2((dest[1]-bot[1]),(dest[0]-bot[0]))
      delta = restrict_angle(bot_a - target_a)
      next_a = arctan2((next_dest[1]-dest[1]),(next_dest[0]-dest[0]))
      theta = restrict_angle(next_a - target_a)
      r = norm(dest-bot)
      #Todo: smoothener, along with setting constants
      
      #Calculate kappa, v and omega
      k = (-1.0 / r) * (k2 * (delta - arctan(-k1 * theta)) + (1 + k1/(1  + (k1 * theta)**2)) * sin(delta))
      vc = v / (1 + beta * (abs(k)**gamma))
      
      w = k*vc
      if w > 10:
        w = 10
      elif w < -10:
        w = -10 
      #~ if r < 0.1:
        #~ vc = 0.05
        #~ w = k*vc
        #~ if w > 10:
          #~ w = 10
        #~ elif w < -10:
          #~ w = -10 
      v_r = vc + b*w/2
      v_l = vc - b*w/2
      
      print "State: ", "bot ",bot,"dest ", dest,"bot_a ", bot_a,"delta ", delta,"theta ", theta,"r ", r
      print "Control: ","k ", k,"vc ", vc,"w ", w,"v_r ", v_r,"v_l ", v_l
      print ""
      #sleep(1)
      
      #Bot propagation
      bot_v = (v_r + v_l)/2
      bot[0] += bot_v*cos(bot_a)*dt
      bot[1] += bot_v*sin(bot_a)*dt
      
      #Environment propagation
      v_ra = v_r + v_al + v_err*normal()
      v_la = v_l + v_err*normal()
      env_v = (v_ra + v_la)/2
      env_w = (v_ra-v_la)/b
      
      env[0] += env_v*cos(env_a)*dt
      env[1] += env_v*sin(env_a)*dt
      env_a = restrict_angle(env_a + env_w*dt)
      
      x.append(env[0])
      y.append(env[1])
      t += dt
      
      err += abs((dest[0]-prev_dest[0])*(prev_dest[1]-env[1])-(dest[1]-prev_dest[1])*(prev_dest[0]-env[0]))*dt/norm(dest-prev_dest)
   
  err /= t*path
  corr /= path
  return [x, y, gx, gy, corr, err]
  



