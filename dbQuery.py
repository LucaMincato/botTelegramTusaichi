from telegram import Update
import sqlite3


# connecting to a database

conn = sqlite3.connect('users.db')
cur = conn.cursor()

list_name = [('Luca', 'Mincato'), ('Emanuele', 'Mincato'), ('Romano', 'Mincato')]

#cur.execute('CREATE TABLE partecipanti1 (name text, surname text)')
#conn.commit

cur.execute("""SELECT * FROM partecipanti1 """)
fetch = cur.fetchall()
conn.commit()

cur.execute("""SELECT surname FROM partecipanti1 """)
fetchSurnam = cur.fetchall()
conn.commit()

inputName = input('inserisci il tuo nome')
inputSurname = input('inserisci il cognonme')

users = (inputName,inputSurname)

if users in fetch:
    print('il cognome esiste già')
else:
    cur.execute(""" INSERT INTO partecipantiBot VALUES (?, ?, ?, ?)""", [inputName, inputSurname,'Nessuna', 'False'])

conn.commit()
conn.close()






conn1 = sqlite3.connect('telegramBot.db')
curs1 = conn1.cursor()
curs1.execute("""SELECT * FROM partecipantiBot """)

for row in (curs1.fetchall()):
    print(row[0])
    if row[0] == 'siamo':
        break	


print(curs1.fetchall())
conn1.commit()
conn1.close()
