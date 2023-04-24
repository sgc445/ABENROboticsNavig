
// CNC_Stepper Control 
//Arjun and Sunil
#include <Wire.h>
#include <string.h>

char distance[20];

const int stepsPerRevolution = 200;

const int StepX = 2;
const int DirX = 5;
const int StepY = 3;
const int DirY = 6;
const int StepZ = 4;
const int DirZ = 7;
const int StepA = 12;
const int DirA = 13;


void setup() {
  Wire.begin();
  Serial.begin(9600);
   
  pinMode(StepX,OUTPUT);
  pinMode(DirX,OUTPUT);
  pinMode(StepY,OUTPUT);
  pinMode(DirY,OUTPUT);
  pinMode(StepZ,OUTPUT);
  pinMode(DirZ,OUTPUT);
  pinMode(DirA,OUTPUT);
  pinMode(StepA,OUTPUT);

// rotate all wheel in same direction
 digitalWrite(DirX, LOW); // set direction, HIGH for clockwise, LOW for anticlockwise
 digitalWrite(DirY, LOW);
 digitalWrite(DirA, HIGH);
 digitalWrite(DirZ, HIGH);

 // turn motor right side
 //digitalWrite(DirX, HIGH);
 //digitalWrite(DirY, LOW);
 //digitalWrite(DirA, LOW);
 //digitalWrite(DirZ, HIGH);

 // turn motor left side
// digitalWrite(DirX, LOW);
 //digitalWrite(DirY, HIGH);
 //digitalWrite(DirA, HIGH);
 //digitalWrite(DirZ, LOW);
 
Serial.println("Master adrunio");
 
}

void move_forward(){
   digitalWrite(DirX, LOW); // set direction, HIGH for clockwise, LOW for anticlockwise
 digitalWrite(DirY, LOW);
 digitalWrite(DirA, HIGH);
 digitalWrite(DirZ, HIGH);
}

void turn_left(){

 // turn motor left side rotate
 digitalWrite(DirX, LOW); // set direction, HIGH for clockwise, LOW for anticlockwise
 digitalWrite(DirY, LOW);
 digitalWrite(DirA, LOW);
 digitalWrite(DirZ, LOW);
  
}


void turn_right(){

 // turn motor left side rotate
 digitalWrite(DirX, HIGH); // set direction, HIGH for clockwise, LOW for anticlockwise
 digitalWrite(DirY, HIGH);
 digitalWrite(DirA, HIGH);
 digitalWrite(DirZ, HIGH);
  
}

void slide_left(){
   digitalWrite(DirX, LOW);
 digitalWrite(DirY, HIGH);
 digitalWrite(DirA, HIGH);
 digitalWrite(DirZ, LOW);
}
void run_motor(){
  
  digitalWrite(StepX,HIGH);
  digitalWrite(StepY,HIGH);
  digitalWrite(StepZ,HIGH);
  digitalWrite(StepA,HIGH);
  delayMicroseconds(600);
  digitalWrite(StepX,LOW);
  digitalWrite(StepY,LOW);
  digitalWrite(StepA,LOW);
  digitalWrite(StepZ,LOW);
  delayMicroseconds(600);

}

int * get_two_distance(){
  
 int dl,dr;
  int init_size = strlen(distance);
  char delim[] = "_";

  char *ptr = strtok(distance, delim);

  int count=0;
 static int dist_array[2];
  while (ptr != NULL)
  {
     if(count==0){
      dl=atoi(ptr);
       dist_array[count]=dl;
     }else{
       dr=atoi(ptr);
       dist_array[count]=dr;
     }
     count=count+1;
    ptr = strtok(NULL, delim);
  }

  
  return dist_array;
}

void loop() {

  for(int x = 0; x<3200; x++) {
  get_distance(2);
  int *di_arr = get_two_distance();
  int dl = *(di_arr+0);
   int dr = *(di_arr+1);
   
  Serial.print(dl);
  Serial.print("\n");
   Serial.print(dr);
    Serial.print("\n");
    delay(1000);
 
  }
  //char distance[2] = {message[0],message[1]};
  //int val = (int)(distance);
  //Serial.println(distance);

  // get current position of the motor using ultrasonic sensor



  // move x1 distance from the start postion x1= and stop

  /*  for(int x = 0; x<3200*2; x++) { 
 run_motor();
  }
 delay(1500000);

*/
  // move x1+x2 stop  12 times distance between  the each plant stand is 2 inch
  
/*for (int y=0;y<23;y++){
  for(int x = 0; x<657; x++) { 
 run_motor();
  }
   delay(10000);

  }
  delay(10000);
  */

  
  delay(1000000);

  move_forward();
for(int x = 0; x<1600; x++) { 
 run_motor();
  }
 delay(5000);
  
  turn_left();
  //slide_left();

 for(int x = 0; x<1600; x++) { 
 run_motor();
  }
 delay(5000);

  move_forward();
for(int x = 0; x<3600; x++) { 
 run_motor();
  }
 delay(5000);

 turn_right();
  //slide_left();

 for(int x = 0; x<1600; x++) { 
 run_motor();
  }
 delay(5000);
 move_forward();

 for (int y=0;y<23;y++){
  for(int x = 0; x<657; x++) { 
 run_motor();
  }
  delay(2000);
 }

  delay(20000);


 
  // end get distance using ultrasonic sensor if distance is greater than 12mm then start to rotate in the direction where ultrasonic distance is higher very high



 // rotate motor towards middle row


// make it stright by sensor if motor total distance is higher than total board length then make it stright , ""


 
//delay(1000); // delay for 1 second



}

void get_distance(int slave)
{ 
  int i = 0;
  
  // Request value from slave
  Wire.requestFrom(slave, 7);
  while(0 < Wire.available())
  {
    distance[i] = Wire.read();
    //Serial.println(distance[i]);
    i++;
  }
  
  distance[i] = '\0';
}
