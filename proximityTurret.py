import RPi.GPIO as GPIO
import time
import argparse
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
 
# Arguments to activate peripherals
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--picamera", type=int, default=-1,
    help="whether or not the Raspberry Pi camera should be used")
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
	
# if a video path was not supplied, grab the reference
# to the webcam
if args.picamera:
        vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
 	# allow the camera or video file to warm up
	time.sleep(2.0)
	
def fire():
	GPIO.output(RelayPin, GPIO.HIGH) #This relay completes the circuit when energized
	print 'FIRING!!! Stay Back you Rouge!'
	time.sleep(2)
	
def loop():
	while True:
		dis = distance()
		print dis, 'cm'
		print ''
		if int(dis) <= 50:
			fire()
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
