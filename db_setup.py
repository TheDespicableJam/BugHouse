import sqlite3

connect = sqlite3.connect('mantis.db')
cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS mantis(id TEXT UNIQUE, role TEXT UNIQUE, pass TEXT UNIQUE)')
cursor.execute('INSERT OR IGNORE INTO mantis (id, role, pass) VALUES ("PRAYING_MANTIS", "OWNER", "KILLTHEEXTERMINATOR"), ("MANTIS1", "MAINTAINER", "CARETAKER"), ("MANTIS2", "MEMBER", "WORKINGRIGHTNOW")')


connect.commit()
connect.close()