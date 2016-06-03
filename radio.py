#!/usr/bin/python2

from time import sleep
from Adafruit_Si4713 import Adafruit_Si4713

FMSTATION = 10480
POWER = 90

def printInfo():
	radio.readASQ()
	print "ASQ:", hex(radio.currASQ), "- InLevel:", radio.currInLevel, "dBfs -",
	radio.readTuneStatus()
	print "Power:", radio.currdBuV, "dBuV - ANTcap:", radio.currAntCap, "- Noise level:", radio.currNoiseLevel

radio = Adafruit_Si4713()

if not radio.begin():
	print "error! couldn't begin!"

else:

	radio.readTuneMeasure(FMSTATION)
	printInfo()

	radio.setTXpower(POWER)
	radio.tuneFM(FMSTATION)

	radio.beginRDS()

	while True:


		printInfo()


		print "turning on"
		radio.setLinzerSchnitteRDS(0x0e, 0xffff, 0x1410)
                sleep(0.5)
                radio.setLinzerSchnitteRDSEmpty()

		sleep(3)

		print "turning off"
		radio.setLinzerSchnitteRDS(0x11, 0xffff, 0x0000)
                sleep(1)
                radio.setLinzerSchnitteRDSEmpty()
		sleep(5)
