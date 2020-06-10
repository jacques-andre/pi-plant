import RPi.GPIO as gpio
import time
import sys
from pushover import init,Client

# pushover
init("<api key>")

pump_pin = 21
soil = 20
sec_to_water = 30

gpio.setmode(gpio.BCM)
gpio.setup(pump_pin, gpio.OUT)
gpio.setup(soil, gpio.IN)


def pump_off():
    gpio.output(pump_pin, gpio.HIGH)


def pump_on():
    gpio.output(pump_pin, gpio.LOW)


def soil_check(seconds):
    if gpio.input(20):
        print("Watering the plant for:" + str(seconds) + "s")
        # off
        pump_on()
        time.sleep(seconds)
        pump_off()
        print("Finished Watering! Now sending push notification...")
        Client("<user key>").send_message(
            "Pumped water to the plants", title="Plants have been watered!"
        )
        gpio.cleanup()
    else:
        pump_off()
        gpio.cleanup()
        print("Sending notification plants already watered!")
        Client("<user key>").send_message(
            "No water pumped to plants", title="Plants have already been watered!"
        )
        sys.exit()


soil_check(sec_to_water)
