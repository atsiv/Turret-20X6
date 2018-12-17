import RPi.GPIO as GPIO
import time
import argparse

# Arguments to activate peripherals
ap = argparse.ArgumentParser()
ap.add_argument("-l", "--laser",
        help="Activates laser for target aquisition")
args =ap.parse_args()

TRIG = 11 #Ultra sonic pin marked TRIG should be connected to RPi GPIO17
ECHO = 12 #Ultra sonic pin marked ECHO should be connected to RPi GPIO18

RelayPin = 13    #Relay should be connected to RPi GPIO27

laserPin = 15    #Laser should be connected to RPi GPIO22

def setup():
	GPIO.setmode(GPIO.BOARD) #Using GPIO's by number, not name

	GPIO.setup(TRIG, GPIO.OUT)   # Setting up ultrasonic GPIO
	GPIO.setup(ECHO, GPIO.IN)

	GPIO.setup(RelayPin, GPIO.OUT)   # Setting up relay GPIO
	GPIO.output(RelayPin, GPIO.HIGH)

	GPIO.setup(laserPin, GPIO.OUT)   # Setting up lasers GPIO
	GPIO.output(laserPin, GPIO.HIGH)

def distance():
	GPIO.output(TRIG, 0)
	time.sleep(0.000002)
	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	while GPIO.input(ECHO) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:
		a = 1
	time2 = time.time()

	during = time2 - time1
	return during * 340 / 2 * 100

if args.laser:
	GPIO.output(laserPin, GPIO.HIGH) #Turns on laser
	print 'Laser Activated'

def loop():
	while True:
		dis = distance()
		print dis, 'cm'
		print ''
		if int(dis) <= 50:
			GPIO.output(RelayPin, GPIO.HIGH) #This relay completes the circuit when energized
			print 'FIRING!!! Stay Back you Rouge!'
			time.sleep(2)
		time.sleep(0.2)
def destroy():
	GPIO.output(laserPin, GPIO.LOW)     # laser off
	GPIO.output(RelayPin, GPIO.LOW)  #relay off
	GPIO.cleanup()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
