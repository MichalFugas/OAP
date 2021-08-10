import RPi.GPIO as GPIO
from time import sleep
from subprocess import call

pin=40

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # sleep(480)

while True:
    print(GPIO.input(pin))
    if GPIO.input(pin) == 1:

        # sleep(5)
        pass
    else:
        print('koniec')
        sleep(0.5)
        if GPIO.input(pin) == 0:
            print('final')
            call("sudo shutdown -h now", shell=True)
