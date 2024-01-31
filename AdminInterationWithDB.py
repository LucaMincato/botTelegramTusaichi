import sqlite3

# conn = sqlite3.connect('telegramBot.db')
# cur = conn.cursor()
# 
# cur.execute('CREATE TABLE partecipantiBot (username text, chatId int, squadra text, tuSaiChi bool)')
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





conn1 = sqlite3.connect('telegramBot.db')
curs1 = conn1.cursor()
sql = f"SELECT squadra,chatId FROM partecipantiBot "
team_and_chat_id = curs1.execute(sql)
conn1.commit()
conn1.close
chat_id_list = []

for row in team_and_chat_id:
    if 'blu' in row:
        i = 0
        chat_id_list.append(row[1])
        i = i + 1
conn1.commit()
conn1.close()

print(chat_id_list)