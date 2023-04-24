# Created by Sunil GC
# Created Date: 7/9/22
# Contributor: Sunil GC,  # add contributor

import Jetson.GPIO as GPIO
import time


# import adafruit_bno055
# import board


class RoboNavigation:
    def __init__(self, en1, in1, in2, en2, in3, in4, trig_n,trig_s,trig_e,trig_w, echo_n, echo_s, echo_w, echo_e):
        self.en1 = en1
        self.in1 = in1
        self.in2 = in2
        self.en2 = en2
        self.in3 = in3
        self.in4 = in4
        self.trig_n = trig_n
        self.trig_s = trig_s
        self.trig_e = trig_e
        self.trig_w = trig_w
        self.echo_n = echo_n
        self.echo_s = echo_s
        self.echo_w = echo_w
        self.echo_e = echo_e

        GPIO.setmode(GPIO.BOARD)
        # initialize EnA, In1 and In2
        GPIO.setup(en1, GPIO.OUT)
        GPIO.setup(in1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(in2, GPIO.OUT, initial=GPIO.LOW)
        # initialize EnA, In3 and In4
        GPIO.setup(en2, GPIO.OUT)
        GPIO.setup(in3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(in4, GPIO.OUT, initial=GPIO.LOW)
        # i2c = board.I2C()
        # sensor = adafruit_bno055.BNO055_I2C(i2c)
        # self.sensor = sensor

        GPIO.setup(trig_n, GPIO.OUT)
        GPIO.setup(trig_s, GPIO.OUT)
        GPIO.setup(trig_e, GPIO.OUT)
        GPIO.setup(trig_w, GPIO.OUT)

        GPIO.setup(echo_n, GPIO.IN)
        GPIO.setup(echo_s, GPIO.IN)
        GPIO.setup(echo_w, GPIO.IN)
        GPIO.setup(echo_e, GPIO.IN)

    def move_forward(self):
        print("forward")
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)

    def move_backward(self):
        print("backward")
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)

    def stop_robot(self, s_t=1):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)
        time.sleep(s_t)

    def turn_left(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)

    def turn_right(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)

    def get_north_reading(self):
        dist = RoboNavigation.get_avg_dis(self,self.trig_n, self.echo_n)
        return dist

    def get_south_reading(self):
        dist = RoboNavigation.get_avg_dis(self,self.trig_s, self.echo_s)
        return dist

    def get_east_reading(self):
        dist = RoboNavigation.get_avg_dis(self,self.trig_e, self.echo_e)
        return dist

    def get_west_reading(self):
        dist = RoboNavigation.get_avg_dis(self,self.trig_w, self.echo_w)
        return dist

    # def get_imu_value(self):
    #     sensor = self.sensor
    #     return sensor.gyro

    def get_avg_dis(self, trig, echo):
        i = 0
        tot = 0
        while (i <= 4):
            tot = tot + RoboNavigation.get_distance(self,trig, echo)
            i = i + 1
        dis = round(tot / 5, 2)
       # print("distance cm: ", dis)
        return dis

    def get_distance(self, trig, echo):
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)
        pulse_start = time.time()
        pulse_end = time.time()

        while GPIO.input(echo) == 0:
            pulse_start = time.time()
            #print("start")
        while GPIO.input(echo) == 1:
            #print("end")
            pulse_end = time.time()
        pulse_duration = (pulse_end - pulse_start)
        distance = pulse_duration * 17150
        return distance
