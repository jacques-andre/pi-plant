import RPi.GPIO as GPIO
import time

channel = 26

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def pump_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn pump on


def pump_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn pump off


pump_on(channel)
print("Pumping")
time.sleep(10)
print("Turning off pump")
pump_off(channel)
time.sleep(1)
GPIO.cleanup()
