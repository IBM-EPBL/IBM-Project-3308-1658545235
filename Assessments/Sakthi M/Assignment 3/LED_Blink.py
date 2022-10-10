#BLINK LED
import RPi.GPIO as GPIO #import raspberry pi GPIO library
from time import sleep

LedPin = 8

def setup():
        GPIO.setmode(GPIO.BOARD)   #use of physical pin numbering
        GPIO.setup(ledPin, GPIO.OUT)
        GPIO.output(ledPin, GPIO.LOW)

def LedBlink():
        while True:
                GPIO.output(LedPin, GPIO.HIGH)
                time.sleep(1)

                GPIO.output(LedPin, GPIO.LOW)
                time.sleep(1)


def EndBlink():
        GPIO.output(ledPin, GPIO.LOW)
        GPIO.cleanup()

if _name_ == '_main_':
        setup()
        try:
                LedBlink()
        except KeyboardInterrupt:
                EndBlink()
