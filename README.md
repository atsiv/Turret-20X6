# Turret-20X6
Automated turret for all of your personal point defense needs

Hardware:
  Raspberry Pi 3b
  Electric Nerf gun
  Relay
  Ultrasonic Sensor
  Laser Module
  Camera

Software:
  Python 3.X (opencv, RPi.GPIO, time and argparse modules)
  openCV
  

For your very own fully functional automated or remote turret, splice the relay in line with mostlikely its only cuircit, and connect the 3 wires of the relay to the RPI, one to 5v, one to ground and the last, the signal pin to physical pin 15.  Connect the TRIG wire on the ultrasonic sensor to pin 11, ECHO to 12 and the last to wires are to 5v and ground to pins 4 and 14 respectivly.  Connect a laser module to a 3.7v pin you like and the SIG wire to pin 15.  Any type of camera may work (really only USB and RPi Camera). 
