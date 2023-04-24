// SLAVE
#include <Wire.h>

#define echoPin1 2
#define trigPin_1 3
#define echoPin2 4
#define trigPin_2 5


char dist[11];

// defines variables
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement

void setup()
{
  Wire.begin(2);
  Wire.onRequest(requestEvent);
 // Wire.onReceive(requestEvent);
  pinMode(trigPin_1, OUTPUT); // Sets the trigPin as an OUTPUT
 pinMode(trigPin_2, OUTPUT);
 // pinMode(trigPin_4, OUTPUT);
  pinMode(echoPin1, INPUT); // Sets the echoPin as an INPUT
 pinMode(echoPin2, INPUT);
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
  Serial.println("Ultrasonic Sensor Test"); // print some text in Serial Monitor  
}

int get_distance(int trigPin,int echoPin)
{
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back) // cm
   Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  return distance;
}
 
void loop()
{
  delay(100);
  //int d1;
  //d1 = get_distance(trigPin_1,echoPin1);
 // Serial.println(d1);
}
 
void requestEvent()
{
  Serial.println("test slave");
  int d1,d2;
  d1 = get_distance(trigPin_1,echoPin1);
  d2 = get_distance(trigPin_2,echoPin2);
  Serial.println(d1);
  
 // d2 = get_distance(trigPin_2,echoPin2);
 
  sprintf(dist, "%d_%d", d1,d2);

  Serial.println(dist);

 // size of this string can vary from 10 up to 15
  Wire.write(dist);
}
