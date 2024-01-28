import sqlite3

# conn = sqlite3.connect('telegramBot.db')
# cur = conn.cursor()
# 
# cur.execute('CREATE TABLE partecipantiBot (username text, chatId int, squadra text, tuSaiChi text)')
# conn.commit

conn1 = sqlite3.connect('telegramBot.db')
curs1 = conn1.cursor()
curs1.execute("""SELECT * FROM partecipantiBot """)
fetchChatId = curs1.fetchall()
print(fetchChatId)

dummy = []

for row in fetchChatId:
    i = 0
    dummy.append(row[0])
    i = i + 1

conn1.commit()
conn1.close()

print(dummy)
