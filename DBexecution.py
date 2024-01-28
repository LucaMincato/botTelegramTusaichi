import sqlite3


def ControlUser(tupla):

    conn = sqlite3.connect('telegramBot.db')
    cur = conn.cursor()

    cur.execute("""SELECT chatId FROM partecipanti2 """)
    fetch = cur.fetchall()
    conn.commit() 

    username = tupla[0]
    chat_id = int(tupla[1])
    chat = (chat_id,)
    
    if chat in fetch:
        return True
    else:
        cur.execute(""" INSERT INTO partecipanti2 VALUES (?, ?)""", [username, chat_id])
        conn.commit()
        conn.close()
        return False

def CheckAddmin(tupla):

    addmin_user_id = '6307311132'
    addmin_username = 'LucaMincato'

    input_username = tupla[0]
    input_chat_id = tupla[1]

    if input_username in addmin_username and input_chat_id in addmin_user_id:
        return True
    else :
        return False
    
def fetchDbChatId():
    conn1 = sqlite3.connect('telegramBot.db')
    curs1 = conn1.cursor()
    fetchChatId = curs1.execute("""SELECT chatId FROM partecipanti2 """)
    chat_id_list = []

    for row in fetchChatId:
        i = 0
        chat_id_list.append(row[0])
        i = i + 1

    conn1.commit()
    conn1.close()
    
    return chat_id_list

