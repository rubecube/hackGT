import os, time 
import serial
import time 
import RPi.GPIO as GPIO 
import glob 
import sys
from subprocess import Popen 
from thread import start_new_thread

import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(18,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(27,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(22,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


## switch 1 is GPIO22
## switch 2 is GPIO18
## switch 3 is GPIO17
## switch 4 is GPIO27
dir="/media/pi/NONAME/Season_1_mp4/"
dir2="/media/pi/NONAME/Season_2_mp4/"

all=[]

ser = serial.Serial('/dev/ttyUSB0',115200)
delaytime = .5

os.chdir(dir)

for file in glob.glob("*.mp4"):
	all.append(dir+file)

os.chdir(dir2)
for file in glob.glob("*.mp4"):
	all.append(dir2+file)

#print(all)
listlen = len(all)
count = 0

AUDIOHANDLER = 0
while True:
	num = random.randint(1,20)
	dur = random.randint(15,60)
	#print(num)
	if GPIO.input(22) or GPIO.input(18) or GPIO.input(27) or GPIO.input(17):
		pick = random.randint(1,4)
		if pick is 1:
			ser.write("G")
			time.sleep(delaytime)
			os.system('aplay /media/pi/NONAME/audio/PickleRick.wav &')
			time.sleep(3)
		if pick is 2:
			ser.write("Y")
			time.sleep(delaytime)
			os.system('aplay /media/pi/NONAME/audio/OgeeRick.wav &' )
			time.sleep(13)
		if pick is 3:
			ser.write("B")		
			time.sleep(delaytime)
			os.system('aplay /media/pi/NONAME/audio/GetYourShtTogether.wav &')
			time.sleep(12)
		if pick is 4:
			ser.write("R")
			time.sleep(delaytime)
			os.system('aplay /media/pi/NONAME/audio/lobaloba.wav &')	
			time.sleep(3)
		if pick is 5:
			os.system('killall omxplayer.bin')
			omxc = Popen(['omxplayer','-b -l '+str(num*60),all[count%listlen]])
			count=(count+1)%listlen
			time.sleep(dur)

#	print "Switch 1 %d Switch 2 %d"%(GPIO.input(22),GPIO.input(18))
#	print "\t\t\tSwitch 3 %d Switch 4 %d"%(GPIO.input(17),GPIO.input(27))
	time.sleep(.001)

#/media/pi/NONAME/audio/PickleRick.wav
#/media/pi/NONAME/audio/OgeeRick.wav
#/media/pi/NONAME/audio/GetYourShtTogether.wav
#/media/pi/NONAME/audio/lobaloba.wav

