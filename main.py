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
inputName = input('inserisci il tuo nome')
inputSurname = input('inserisci il cognonme')

for row in fetch:
    nameFetched = row[0]
    surnameFetched = row[1]
    if inputName.strip() not in nameFetched and inputSurname.strip() not in surnameFetched:
        print('checking')
    else:
        print('il cognome esiste già')
        break
    cur.execute(""" INSERT INTO partecipanti1 VALUES (?, ?)""", [inputName, inputSurname])

conn.commit()
conn.close()

conn1 = sqlite3.connect('users.db')
curs1 = conn1.cursor()
curs1.execute("""SELECT * FROM partecipanti1 """)
print(curs1.fetchall())
conn1.commit()
conn1.close()
