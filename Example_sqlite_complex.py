#!/usr/bin/env python3
#
# This exemple is more related to the raspberry pi
# The cpu temperature is recorded aside the external measures of the AM2320
#
# in case of function fail the value is set to 0
#
import sqlite3
import datetime
import subprocess
import AM2320
#
# ability to change db filename is usefull on initial setup and debug
dbname = 'monitoring.sqlite'
#
# -------------------- GET DATE --------------------
actual_date = str(datetime.datetime.now())
#
# -------------------- GET CPU TEMPERATURE --------------------
try:
	cpu_temp = subprocess.check_output(["cat", "/sys/class/thermal/thermal_zone0/temp"], universal_newlines=True)
	cpu_temp = int(cpu_temp)/1000
except:
	cpu_temp = 0
# -------------------- GET EXTERNAL TEMPERATURE & HUMIDITY --------------------
try:
	sensor = AM2320.AM2320()
	sensor.get_data()
	case_temp = sensor.temperature
	case_humi = sensor.humidity
except:
	case_temp = 0
	case_humi = 0
#
# -------------------- LOG IN DATABASE --------------------
consqlite = sqlite3.connect(dbname)
cur = consqlite.cursor()
# create database
cur.execute('''CREATE TABLE IF NOT EXISTS temperatures
             (date text, cpu_temp float, case_temp float, case_humi float)''')
# insert data
cur.execute('''INSERT INTO temperatures (date,cpu_temp, case_temp,case_humi) VALUES( ' '''
	+ str(actual_date) + ''' ',' '''
	+ str(cpu_temp) + ''' ',' '''
	+ str(case_temp) + ''' ',' '''
	+ str(case_humi) + ''' ')''')
# commit and close db
consqlite.commit()
consqlite.close()
