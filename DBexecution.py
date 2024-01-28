import sqlite3


def ControlUser(tupla):
    username = tupla[0]
    chat_id = tupla[1]

    if checkUserId(chat_id):

        return True
    
    else:
        conn = sqlite3.connect('telegramBot.db')
        cur = conn.cursor()
        cur.execute(""" INSERT INTO partecipanti2 VALUES (?, ?)""", [username, chat_id])
        conn.commit()
        conn.close()

        return False
    

def CheckAddmin(adminId):

    addmin_user_id = '6307311132'

    input_chat_id = adminId

    if input_chat_id in addmin_user_id:
        return True
    else:
        return False
    

def checkUserId(userId):
    conn = sqlite3.connect('telegramBot.db')
    cur = conn.cursor()

    cur.execute("""SELECT chatId FROM partecipanti2 """)
    fetch = cur.fetchall()
    conn.commit()
    conn.close
    chat_id = int(userId)
    chat = (chat_id,)
    if chat in fetch:
        return True
    else:
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

