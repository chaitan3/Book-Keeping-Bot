#include <Max3421e.h>
#include <Usb.h>
#include <AndroidAccessory.h>
#include <util/delay.h>
 
#define MAX_BUF 128 
#define COMMAND_LENGTH 12
#define LOOP_TIME 10
#define SPEED 1
#define PWM_SPEED 0
#define PWM_LEFT 1
#define PWM_RIGHT 2
#define FORWARD_LEFT 3
#define FORWARD_RIGHT 4
#define REVERSE_LEFT 5
#define REVERSE_RIGHT 6
#define X_ANGLE 0
#define TURN_TIME 10

/*AndroidAccessory acc("IITB",
		     "BookBot",
		     "Book Keeping Bot",
		     "1.0",
		     "http://www.android.com",
		     "0000000012345678");*/

AndroidAccessory acc("Google, Inc.",
		     "DemoKit",
		     "DemoKit Arduino Board",
		     "1.0",
		     "http://www.android.com",
		     "0000000012345678");

char msg[MAX_BUF];
int len;
char confirm[10];
float curr_x, curr_y, next_x, next_y;
float angle, mag_angle, diff;
  
void setup()
{
  Serial.begin(115200);
  Serial.print("\rStart\r");
  acc.powerOn(); 
  get_next_point();
  curr_x = next_x;
  curr_y = next_y;
  
  /*pinMode(PWM_LEFT, OUTPUT);
  pinMode(PWM_RIGHT, OUTPUT);
  pinMode(FORWARD_LEFT,OUTPUT);
  pinMode(FORWARD_RIGHT, OUTPUT);
  pinMode(REVERSE_LEFT,OUTPUT);
  pinMode(REVERSE_RIGHT, OUTPUT);*/
}

void get_next_point() 
{
  if (acc.isConnected()) { 
    Serial.println("Connected\r");
    do {
      len = acc.read(msg, COMMAND_LENGTH, MAX_BUF);  
    }while(len == -1);
    msg[COMMAND_LENGTH] = '\0';
    Serial.println("Received");
    Serial.println(msg);
    sscanf(msg, "GO %f %f ", &next_x, &next_y);    
  }
}
void send_confirm()
{
 if (acc.isConnected()) { 
    strcpy(confirm, "aheaden");
    acc.write((void *)confirm, strlen(confirm));              
  }
}
void loop()
{
  if((abs(curr_x-next_x) < 1e-5) && (abs(curr_x-next_x) < 1e-5))
  {
    /*analogWrite(PWM_LEFT, 0);
    analogWrite(PWM_RIGHT, 0);*/
    send_confirm();
    get_next_point();
    angle = atan((next_y-curr_y)/(next_x-curr_x));
    //turn code
    do {
      //confirm units, mag_angle range, turn anti-clockwise?
      mag_angle = 0;
      mag_angle -= X_ANGLE;
      diff = angle - mag_angle;
      /*analogWrite(PWM_LEFT, PWM_SPEED);
      analogWrite(PWM_RIGHT, PWM_SPEED);
      digitalWrite(FORWARD_LEFT, HIGH);
      digitalWrite(FORWARD_RIGHT, LOW);
      digitalWrite(REVERSE_RIGHT, HIGH);
      digitalWrite(REVERSE_LEFT, LOW);*/
      _delay_ms(TURN_TIME*abs(diff));
    }
    while(abs(diff) > 1e-5);
    
    /*analogWrite(PWM_LEFT, PWM_SPEED);
    analogWrite(PWM_RIGHT, PWM_SPEED);
    digitalWrite(FORWARD_LEFT, HIGH);
    digitalWrite(FORWARD_RIGHT, HIGH);
    digitalWrite(REVERSE_RIGHT, LOW);
    digitalWrite(REVERSE_LEFT, LOW);*/
  }
  curr_x += SPEED*LOOP_TIME*cos(angle);
  curr_y += SPEED*LOOP_TIME*sin(angle);
  _delay_ms(LOOP_TIME);
  
  //laser code
}
