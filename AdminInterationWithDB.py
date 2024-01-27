import sqlite3

#conn = sqlite3.connect('telegramBot.db')
#cur = conn.cursor()
#
#cur.execute('CREATE TABLE partecipanti2 (username text, chatId int)')
#conn.commit

conn1 = sqlite3.connect('telegramBot.db')
curs1 = conn1.cursor()
fetchChatId = curs1.execute("""SELECT chatId FROM partecipanti2 """)
print(fetchChatId)

dummy = []

for row in fetchChatId:
    i = 0
    dummy.append(row[0])
    i = i + 1

conn1.commit()
conn1.close()

print(dummy)
