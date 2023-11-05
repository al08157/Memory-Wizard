import sqlite3
import csv

# create database connection
conn = sqlite3.connect('building.db')

# create table
cur = conn.cursor()
cur.execute('CREATE TABLE building (S_no INTEGER, x REAL, y REAL, address TEXT, name TEXT)')

# read CSV and insert data into table
with open('building.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for row in reader:
        cur.execute('INSERT INTO building VALUES (?, ?, ?, ?, ?)', row)

# commit changes and close connection
conn.commit()
conn.close()
