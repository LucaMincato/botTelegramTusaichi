from telegram import Update
import sqlite3


# connecting to a database

conn = sqlite3.connect('users.db')

conn.close()
