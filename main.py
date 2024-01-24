from telegram import Update
import sqlite3


# connecting to a database

conn = sqlite3.connect('users.db')
cur = conn.cursor()

list_name = [('Luca', 'Mincato'), ('Emanuele', 'Mincato'), ('Romano', 'Mincato')]

# cur.execute('''CREATE TABLE users (first name TEXT, last name TEXT)''')
# conn.commit

cur.executemany('''INSERT INTO users VALUES (?,?)''', list_name)
conn.commit

cur.close()
conn.close()
