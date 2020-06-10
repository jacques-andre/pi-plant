import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

if GPIO.input(21):
    # off
    print("Soil is not wet")
else:
    # on
    print("Soil is wet!")
