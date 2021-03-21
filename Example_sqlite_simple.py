#!/usr/bin/env python3
#
# Will get data & time, then store on sqlite3
# This script is aimed to be called with crontab of the rapsberry (for example every 10 minutes)
# Otherwise it is possible to add an infinite loop with a sleep instruction
#
import sqlite3
import datetime
import AM2320
# -------------------- GET DATA --------------------
# from actual date and time
actual_date = str(datetime.datetime.now())
# from the AM2320
sensor = AM2320.AM2320()
sensor.get_data()
# -------------------- RECORD IN SQLITE --------------------
# create sqlite object
consqlite = sqlite3.connect('monitor.sqlite')
cur = consqlite.cursor()
# cerate a table named 'trend'
cur.execute('''CREATE TABLE IF NOT EXISTS trend
             (date text, temperature float, humidity float)''')
# insert data inside the table
cur.execute('''INSERT INTO trend (date,temperature,humidity) VALUES( ' '''
            + str(actual_date) + ''' ',' '''
            + str(sensor.temperature) + ''' ',' '''
            + str(sensor.humidity) + ''' ')''')
# commit and close connection
consqlite.commit()
consqlite.close()
