import sqlite3

#conn = sqlite3.connect('telegramBot.db')
#cur = conn.cursor()
#
#cur.execute('CREATE TABLE partecipanti (username text, chatId text)')
#conn.commit

conn1 = sqlite3.connect('telegramBot.db')
curs1 = conn1.cursor()
curs1.execute("""SELECT * FROM partecipanti """)
print(curs1.fetchall())
conn1.commit()
conn1.close()


