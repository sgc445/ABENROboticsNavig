import RPi.GPIO as GPIO
import time

# for 1st Motor on ENA
ENA = 33
IN1 = 21
IN2 = 22

# set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)

# initialize EnA, In1 and In2
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)

# Stop
GPIO.output(ENA, GPIO.HIGH)
#GPIO.output(IN1, GPIO.LOW)
#GPIO.output(IN2, GPIO.LOW)
#time.sleep(2)

# Forward
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)
time.sleep(5)

# Stop
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
time.sleep(2)

# Backward
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.HIGH)
time.sleep(2)

# Stop
GPIO.output(ENA, GPIO.LOW)
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
time.sleep(2)

GPIO.cleanup()
