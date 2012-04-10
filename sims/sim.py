from pylab import *

#sensor error modelling, bot destination check
#Error plots pitch, speed, different trajectories

def simulate(n, l, initial, init_a, dests, v, c_slip=4e-2, c_mag=1e-1, c_align=1e-1 ):

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
  gy=delete(gy,2)

  #Slippage error
  v_err = v*(c_slip)
  #Motor alignment error
  al_err = v*(c_align)
  v_al = 0

  #Sensor Angle error 
  a_err = c_mag

  #Time step 
  dt = 1e-2
  t = 0
  #Error
  err = 0

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
    a = arctan2(dest[1]-bot[1],dest[0]-bot[0])
    return [a + a_err*normal(), a, al_err*normal()]

  for dest in dests:
    
    [env_a,bot_a, v_al] = turn()
    
    no_x = 0
    no_y = 0

    while norm(bot-dest) > 1e-2:
      env[0] += (v + v_al + v_err*normal())*cos(env_a)*dt
      env[1] += (v + v_err*normal())*sin(env_a)*dt
      
      bot[0] += v*cos(bot_a)*dt
      bot[1] += v*sin(bot_a)*dt
      
      hit = horiz_grid() 
      if hit:
        no_y = hit
        bot[1] = env[1]
        [env_a,bot_a, v_al] = turn()
        
      hit = vert_grid()
      if hit:
        no_x = hit
        bot[0] = env[0]
        [env_a,bot_a, v_al] = turn()
      
      x.append(env[0])
      y.append(env[1])
      t += dt
      
      err += abs((dest[0]-prev_dest[0])*(prev_dest[1]-env[1])-(dest[1]-prev_dest[1])*(prev_dest[0]-env[0]))*dt/norm(dest-prev_dest)
   
    prev_dest = dest.copy()

  err /= t
  return [x, y, gx, gy, err]
  



