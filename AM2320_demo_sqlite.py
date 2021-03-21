#!/usr/bin/env python3
#
# Will get data & time then store on sqlite
# This script is aimed to be called with crontab in example
# Otherwise we can add a while loop with a sleep instruction
#
import time
import sqlite3
import datetime
#
import AM2320


# -------------------- GET DATA --------------------

actual_date = str(datetime.datetime.now())
sensor = AM2320.AM2320()
sensor.get_data()

# -------------------- RECORD SQLITE --------------------
consqlite = sqlite3.connect('monitor.sqlite')
cur = consqlite.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS trend
             (date text, temperature float, humidity float)''')

cur.execute('''INSERT INTO trend (date,temperature,humidity) VALUES( ' '''
            + str(actual_date) + ''' ',' '''
            + str(sensor.temperature) + ''' ',' '''
            + str(sensor.humidity) + ''' ')''')

consqlite.commit()
consqlite.close()
