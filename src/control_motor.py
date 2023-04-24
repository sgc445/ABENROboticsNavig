import time

import RPi.GPIO as GPIO
from time import sleep


def go_forward(input1, input2):
    print("forward")
    GPIO.output(input1, GPIO.HIGH)
    GPIO.output(input2, GPIO.LOW)


def go_backward(input1, input2):
    print("backward")
    GPIO.output(input1, GPIO.LOW)
    GPIO.output(input2, GPIO.HIGH)


def stop_motor(input1, input2):
    GPIO.output(input1, GPIO.LOW)
    GPIO.output(input2, GPIO.LOW)


def void_setup(in1, in2, in3, in4, en1, en2):
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)
    GPIO.setup(en2, GPIO.OUT)
    # initialize EnA, In1 and In2
    GPIO.setup(en1, GPIO.OUT)
    GPIO.setup(in1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(in2, GPIO.OUT, initial=GPIO.LOW)


if __name__ == '__main__':
    GPIO.cleanup()
    from Jetson.GPIO import gpio_pin_data
    model, JETSON_INFO, _channel_data_by_mode = gpio_pin_data.get_data()
    print(model)
    print(JETSON_INFO)

    # first motor
    mot1_in1 = 21
    mot1_in2 = 22
    enable1 = 33
    # second motor
    enable2 = 33
    mot2_in1 = 23
    mot2_in2 = 24



    # setup
    void_setup(mot1_in1, mot1_in2, mot2_in1, mot2_in2, enable1, enable2)
   # GPIO.output(enable1, GPIO.HIGH)

    #stop_motor(mot1_in1, mot1_in2)

    p1 = GPIO.PWM(enable1, 500)
    p1.start(20)
    #p1.ChangeDutyCycle(50)

    go_forward(mot1_in1, mot1_in2)
    time.sleep(5)

    stop_motor(mot1_in1, mot1_in2)
    time.sleep(1)


    go_backward(mot1_in1, mot1_in2)
    time.sleep(5)

    stop_motor(mot1_in1, mot1_in2)
    time.sleep(1)

    GPIO.cleanup()
    print("end")
