#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

from RaspiCorder import Menus
from RaspiCorder import Recorder

sleepTime = 0.25

# Initialization of the plate
lcd = Adafruit_CharLCDPlate.Adafruit_CharLCDPlate()
lcd.begin(16,2)
lcd.clear()
lcd.message("  Introducing\n  RaspiCorder")
sleep(2)
lcd.clear()

# Definition of utility functions
def instrumentInput():
	instmenu = Menus.InstrumentMenu()
	instSelection = instmenu.getInstrumentInput(lcd)
	lcd.clear()
	return instSelection

def recConfirm(instName):
	recmenu = Menus.ConfirmationMenu(lcd, instName)
	recSelect = recmenu.InstrumentConfirm()
	lcd.clear()
	return recSelect

def record(instName):
	rec = Recorder.Recorder(instName)
	rec.record()


# Menu logic
while True:
	inst = instrumentInput()
	instName = Menus.Instrument.instrumentName(inst)
	sleep(sleepTime)

	beginRecording = recConfirm(instName)
	sleep(sleepTime)

	if not beginRecording:
		continue

	lcd.clear()
	lcd.message("recording...")
	record(instName)
	lcd.clear()
	lcd.message("recording complete")
	sleep(sleepTime * 4)
	lcd.clear()