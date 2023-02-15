import board
import digitalio
import busio
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

# Built in LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
ow_bus = OneWireBus(board.GP0)
print("Found devices: " + str(ow_bus.scan()))
sens1 = DS18X20(ow_bus, ow_bus.scan()[0])

# Connect to Master and send initial connection ping
uart = busio.UART(tx=board.GP4, rx=board.GP5, baudrate=9600, timeout=0)

while True:
    led.value = True
    print("sensor 1: " + str(sens1.temperature))
    uart.write(bytes(f"<1,{str(sens1.temperature)}>", "ascii"))
    print("Sent temperature data to master")