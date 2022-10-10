#Traffic Lights

#import library files
import RPi.GPIO as GPIO
import time
import signal
import sys


#configure rasperry pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)


def LightOff(signal, frame):
    GPIO.output(9, False)
    GPIO.output(10, False)
    GPIO.output(11, False)
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, LightOff)

while True:
    GPIO.output(9, True) #RED
    time.sleep(5)
    GPIO.output(10, True)
    time.sleep(5)

    GPIO.output(9, False) #GREEN
    GPIO.output(10, False)
    GPIO.output(11, True)
    time.sleep(5)

    GPIO.output(11, False) #YELLOW
    GPIO.output(10, True)
    time.sleep(5)

    GPIO.output(10, False)
