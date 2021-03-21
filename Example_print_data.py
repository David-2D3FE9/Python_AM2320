#!/usr/bin/python
#
# This example get the data from sensor then print it on the terminal
#
import time
import AM2320
#
#Create an object from the AM2320 class called "sensor"
sensor = AM2320.AM2320()
#
#Infinite loop for example
while True:
	# Request a read from the sensor
	sensor.get_data()
	# Get the data from the `sensor` object
	temperature_C = sensor.temperature
	temperature_F = (sensor.temperature * 9/5) + 32
	humidity = sensor.humidity
	#Print the data
	print(str(temperature_C) + " degrees C")
	print(str(temperature_F) + " degrees F")
	print(str(humidity) + " %R\n")
	#Delay and repeat
	time.sleep(3)
