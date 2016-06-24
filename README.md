# Python class for connecting to the Adafruit Si4713 (FM transmitter) breakout-board

## LinzerSchnitte fork

This is a fork of a library to use the Adafruit Si4713 FM transmitter module on a Raspberry Pi. It is adapted for use with the [LinzerSchnitte](http://www.aec.at/linzerschnitte) FM receiver device. It uses RDS group 6 to communicate with the LinzerSchnitte receivers. Group 6 functionality is not present in the upstream codebase.

## How to use

Connect the board's I2C pins to the RPi I2C pins and the reset pin to GPIO4 (right next to the I2C/SPI pins). You can use 5V or 3V3 to power the board.

Adapt `radio.py` to your liking. You will want to set `FMSTATION` to the frequency you use. The main loop sets all LinzerSchnitte devices to particular on/off patterns; take a look at the [LinzerSchnitte RDS commands](http://www.aec.at/linzerschnitte/wiki/index.php/RDS_Commands) and `linzerschnitte.py` to understand how to activate different patterns for devices with particular addresses/groups.

## Note regarding the base of this fork

Code reused from Adafruit's example code and Hansipete's original code. Converted into a reusable class by djazz/daniel-j. Uses Adafruit_I2C and RPi.GPIO, make sure those are available!

Original code is from this Adafruit forums thread:
https://forums.adafruit.com/viewtopic.php?f=50&t=58453

This file is included in this repo:
https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_I2C/Adafruit_I2C.py

Don't forget to enable I2C! If you're on Raspbian, use `sudo raspi-config` and enable it.
