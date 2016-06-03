#!/usr/bin/python2

from time import sleep
from Adafruit_Si4713 import Adafruit_Si4713

FMSTATION = 10100
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

		radio.setLinzerSchnitteRDS(0x03, 0xffff, 0x001a)
		sleep(5)
