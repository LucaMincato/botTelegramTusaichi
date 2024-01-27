import sqlite3

# conn = sqlite3.connect('telegramBot.db')
# cur = conn.cursor()
# 
# cur.execute('CREATE TABLE partecipanti2 (username text, chatId int)')
# conn.commit

conn1 = sqlite3.connect('telegramBot.db')
curs1 = conn1.cursor()
curs1.execute("""SELECT chatId FROM partecipanti2 """)
print(curs1.fetchall())
conn1.commit()
conn1.close()


