import sqlite3
conn = sqlite3.connect('name.db')
c = conn.cursor()

points = sqlite3.connect('points.db')
p = points.cursor()
import datetime as time

now = time.datetime.now()
hour = now.hour

c.execute('CREATE TABLE IF NOT EXISTS points(point INTEGER)')
