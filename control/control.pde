#define pi 3.1415926

#include <Wire.h>
int HMC6352SlaveAddress = 0x42;
int HMC6352ReadAddress = 0x41; //"A" in hex, A command is: 

float restrict_angle(float a) {
	if (a > pi)
		return restrict_angle(a - 2*pi);
	else if(a < -pi)
		return restrict_angle(a + 2*pi);
	return a;
}

float v= 0.1571;
float env_a = pi/2, bot_a = pi/2;
float env[2] = {0,0};
float bot[2] = {0,0};
float prev_dest[2] = {0,0};
float next_dest[2];
float b = 0.175, l=10;
float dt = 0.1;
int i;
#define n 10
float dests[n][2];
float k1=1,k2=100,beta=0.1,gamma=0.4;
float earth=0.0;

void setup() {
  Serial.begin(115200);
  pinMode(27,OUTPUT);
  pinMode(28,OUTPUT);
  pinMode(24,OUTPUT);
  pinMode(25,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  
  for(i=0;i<n;i++)
  {
    dests[i][0] = (i+1)*l/n;
    dests[i][1] = dests[i][0];
  }
  i=0;
  
  HMC6352SlaveAddress = HMC6352SlaveAddress >> 1; // I know 0x42 is less than 127, but this is still required
  Wire.begin();
}

float get_mag()
{
   //"Get Data. Compensate and Calculate New Heading"
  Wire.beginTransmission(HMC6352SlaveAddress);
  Wire.send(HMC6352ReadAddress);              // The "Get Data" command
  Wire.endTransmission();

  //time delays required by HMC6352 upon receipt of the command
  //Get Data. Compensate and Calculate New Heading : 6ms
  delay(6);

  Wire.requestFrom(HMC6352SlaveAddress, 2); //get the two data bytes, MSB and LSB

  //"The heading output data will be the value in tenths of degrees
  //from zero to 3599 and provided in binary format over the two bytes."
  byte MSB = Wire.receive();
  byte LSB = Wire.receive();

  float headingSum = (MSB << 8) + LSB; //(MSB / LSB sum)
  float headingInt = headingSum / 10;
  return headingInt;
}


float bot_v,dest[2];
float v_r,v_l,vc,w,k,delta,theta,target_a,next_a,r;

void loop() {
  dest[0] = dests[i][0];
  dest[1] = dests[i][1];
  if (i>0) {
    prev_dest[0] = dests[i-1][0];
    prev_dest[1] = dests[i-1][1];
  }
  if (i<n-1) {
    next_dest[0] = dests[i+1][0];
    next_dest[1] = dests[i+1][1];
  }
  else {
    next_dest[0] = 2*dests[i][0]-dests[i-1][0];
    next_dest[1] = 2*dests[i][1]-dests[i-1][1];
  }
  r = 1;
  while(r>0.1) {
    bot_a = (get_mag()-earth)*(pi/180); 
    
    target_a = atan2(dest[1]-bot[1],dest[0]-bot[0]);
    delta = restrict_angle(bot_a - target_a);
    next_a = atan2((next_dest[1]-dest[1]),(next_dest[0]-dest[0]));
    theta = restrict_angle(next_a - target_a);
    r = sqrt(pow(dest[1]-bot[1],2)+pow(dest[0]-bot[0],2));
    k = (-1.0 / r) * (k2 * (delta - atan(-k1 * theta)) + (1 + k1/(1  + pow(k1 * theta,2))) * sin(delta));
    vc = v / (1 + beta * pow(fabs(k),gamma));
    w=k*vc;
    if (w>10)
      w = 10;
    else if (w<-10)
      w = -10;
     v_r = vc + b*w/2;
     v_l = vc - b*w/2;
    Serial.println("Start");
    Serial.print("destx=");
    Serial.println(dest[0]);
    Serial.print("desty=");
    Serial.println(dest[1]);
    Serial.print("v_r=");
    Serial.println(v_r);
    Serial.print("v_l=");
    Serial.println(v_l);
    Serial.print("r=");
    Serial.println(r);
    Serial.print("theta=");
    Serial.println(theta);
    Serial.print("delta=");
    Serial.println(delta);
    Serial.print("k=");
    Serial.println(k);
    Serial.print("vc=");
    Serial.println(vc);
    Serial.print("w=");
    Serial.println(w);
    
    set_right_speed();
    set_left_speed();
    
    delay(1000*dt);
    
    bot_v = (v_r + v_l)/2;
    bot[0] += bot_v*cos(bot_a)*dt;
    bot[1] += bot_v*sin(bot_a)*dt;
    //temporary fix
    bot_a = restrict_angle(bot_a + w*dt);
  }
  i++;
}

void set_left_speed() {
  int pwm = v_l*255/v;
  if (v_l > 0) {
    digitalWrite(28,HIGH);
    digitalWrite(27,LOW);
  }
  else {
    digitalWrite(28,LOW);
    digitalWrite(27,HIGH);
  }
  analogWrite(6, 255-pwm); 
}
void set_right_speed() {
  int pwm = v_r*255/v;
  if (v_r > 0) {
    digitalWrite(25,HIGH);
    digitalWrite(24,LOW);
  }
  else {
    digitalWrite(25,LOW);
    digitalWrite(24,HIGH);
  }
  analogWrite(5, 255-pwm); 
}
