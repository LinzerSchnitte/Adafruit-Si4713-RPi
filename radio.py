#!/usr/bin/python2

from time import sleep
from Adafruit_Si4713 import Adafruit_Si4713
import linzerschnitte

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


		print "turning on group FFF1"
		radio.setLinzerSchnitteRDS(linzerschnitte.CMD_PATTERN_BREATH,
                                           0xfff1,
                                           linzerschnitte.pattern_ramps(850, 100))
                sleep(0.5)
                radio.setLinzerSchnitteRDSEmpty()

		sleep(5)

                print "turning on group FFD0"
		radio.setLinzerSchnitteRDS(linzerschnitte.CMD_PATTERN_TWINKLE,
                                           0xffd0,
                                           linzerschnitte.pattern_ramps(850, 100))
                sleep(0.5)
                radio.setLinzerSchnitteRDSEmpty()

		sleep(5)

		print "turning off"
		radio.setLinzerSchnitteRDS(linzerschnitte.CMD_PATTERN_OFF,
                                           linzerschnitte.ADDRESS_ALL,
                                           linzerschnitte.ZERO)
                sleep(1)
                radio.setLinzerSchnitteRDSEmpty()
		sleep(3)
