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
        return 0
    else:
        cur.execute(""" INSERT INTO partecipanti2 VALUES (?, ?)""", [username, chat_id])
        conn.commit()
        conn.close()
        return 1

def CheckAddmin(tupla):

    addmin_user_id = '6307311132'
    addmin_username = 'LucaMincato'

    input_username = tupla[0]
    input_chat_id = tupla[1]

    if input_username in addmin_username and input_chat_id in addmin_user_id:
        return 1
    else :
        return 0