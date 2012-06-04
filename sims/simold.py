from pylab import *

#sensor error modelling, bot destination check
#Error plots pitch, speed, different trajectories

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
  #Speed of left and right wheels
  v_r = v + v_al
  v_l = v

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
  #Count 
  count = 0

  #Path length
  path = 0.0

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

  def turn():
    #Desired orientation according to the bot
    a = arctan2(dest[1]-bot[1],dest[0]-bot[0])
    #return actual environment orientation
    return a + a_err*normal()

  for dest in dests:
    
    env_a = turn()
    
    no_x = 0
    no_y = 0

    path += norm(dest-prev_dest)

    while (bot[0] < dest[0]) and (bot[1] < dest[1]):
      hit = horiz_grid() 
      if hit:
        no_y = hit
        #reset y coordinate
        bot[1] = env[1]
        env_a = turn()
        #Increment the number of corrections
        corr += 1
        
      hit = vert_grid()
      if hit:
        no_x = hit
        #reset x coordinate
        bot[0] = env[0]
        env_a = turn()
        corr += 1
        
      #corrections every 10 time steps
      if count == 10:
        count = 0
        env_a = turn()
      count += 1
      
      #Bot reads magnetometer
      bot_a = env_a + a_err*normal()
      
      
      
      #Bot propagation
      bot_v = (v_r + v_l)/2
      bot[0] += bot_v*cos(bot_a)*dt
      bot[1] += bot_v*sin(bot_a)*dt
      
      #Environment propagation
      v_ra = v_r + v_err*normal()
      v_la = v_l + v_err*normal()
      env_v = (v_ra + v_la)/2
      w = (v_ra-v_la)/b
      
      env[0] += env_v*cos(env_a)*dt
      env[1] += env_v*sin(env_a)*dt
      env_a += w*dt
      
      x.append(env[0])
      y.append(env[1])
      t += dt
      
      err += abs((dest[0]-prev_dest[0])*(prev_dest[1]-env[1])-(dest[1]-prev_dest[1])*(prev_dest[0]-env[0]))*dt/norm(dest-prev_dest)
   
    prev_dest = dest.copy()

  err /= t*path
  corr /= path
  return [x, y, gx, gy, corr, err]
  



