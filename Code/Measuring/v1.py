import board
import digitalio
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

# Built in LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

ow_bus = OneWireBus(board.GP0)
sens1 = DS18X20(ow_bus, ow_bus.scan()[0])
while True:
    led.value = True
    print("sensor 1: " + str(sens1.temperature))