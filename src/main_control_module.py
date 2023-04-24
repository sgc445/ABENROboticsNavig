# Created by Sunil GC
# Created Date: 6/1/22
# Contributor: Sunil GC, Arjun Upadhaya  # add contributor
import sys
import argparse
from robot_navigation import RoboNavigation
import Jetson.GPIO as GPIO
import time


def navigation():
    # set up motor pin
    print("::::")
    GPIO.cleanup()

    # first motor
    enable1 = 32
    mot1_in1 = 21
    mot1_in2 = 22

    # second motor
    enable2 = 33
    mot2_in1 = 23
    mot2_in2 = 24

    # ultrasonic sensor
    trig_n = 36
    trig_s = 16
    trig_e = 35
    trig_w = 26
    echo_n = 38
    echo_s = 15
    echo_e = 40
    echo_w = 37

    rb = RoboNavigation(enable1, mot1_in1, mot1_in2, enable2, mot2_in1, mot2_in2, trig_n, trig_s, trig_e, trig_w,
                        echo_n, echo_s, echo_w, echo_e)

    print("south", rb.get_south_reading())
    print("west", rb.get_west_reading())
    print("east", rb.get_east_reading())
    print("north", rb.get_north_reading())

    # set up duty cycle
    p1 = GPIO.PWM(enable1, 500)
    p1.start(25)

    p2 = GPIO.PWM(enable2, 500)
    p2.start(25)

    rb.move_forward()
    time.sleep(2)
    rb.stop_robot()

    if rb.get_east_reading() <= 30:
        rb.turn_left()
        time.sleep(1)
        rb.stop_robot()

        # move forward
        rb.move_forward()
        time.sleep(2)
        rb.stop_robot()

        # turn  right
        rb.turn_right()
        time.sleep(1)
        rb.stop_robot()

        for i in range(23):
            rb.move_forward()
            time.sleep(1)
            rb.stop_robot()
            time.sleep(1)

        rb.turn_left()
        time.sleep(3)
        rb.stop_robot()

        rb.move_forward()
        time.sleep(5)
        rb.stop_robot()

        rb.turn_left()
        time.sleep(3)
        rb.stop_robot()

        rb.move_forward()
        time.sleep(12)
        rb.stop_robot()

    else:
        rb.turn_right()
        time.sleep(1)
        rb.stop_robot()
        # move forward
        rb.move_forward()
        time.sleep(2)
        rb.stop_robot()
        # turn left
        rb.turn_left()
        time.sleep(1)
        rb.stop_robot()
        for i in range(23):
            rb.move_forward()
            time.sleep(1)
            rb.stop_robot()
            time.sleep(2)

        rb.turn_right()
        time.sleep(3)
        rb.stop_robot()

        rb.move_forward()
        time.sleep(5)
        rb.stop_robot()

        rb.turn_right()
        time.sleep(3)
        rb.stop_robot()

        rb.move_forward()
        time.sleep(12)
        rb.stop_robot()


    GPIO.cleanup()
    print("end")


# This is the main function
def main(_):
    # Initiate with argument parser
    parser = argparse.ArgumentParser(
        description="Robot Control Script")
    parser.add_argument("-f",
                        "--in_flag",
                        help="Any flag = True",
                        type=str, nargs='?')

    args = parser.parse_args()

    mode = GPIO.getmode()
    print(mode)

    # robot navigation
    navigation()

    # Image Acquisition from realsense


if __name__ == '__main__':
    print("__________________________________Robot Control start________________________________")
    main(sys.argv)
