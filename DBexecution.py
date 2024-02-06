import sqlite3


def ControlUser(tupla):
    username = tupla[0]
    chat_id = tupla[1]

    if checkUserId(chat_id):

        return True
    
    else:
        conn = sqlite3.connect('telegramBot.db')
        cur = conn.cursor()
        cur.execute(""" INSERT INTO partecipantiBot VALUES (?, ?, ?, ?)""", [username, chat_id, 'Nessuna', 'False'])
        conn.commit()
        conn.close()

        return False
    

def CheckAddmin(adminId):

    addmin_user_id = 6307311132

    if adminId == addmin_user_id:
        return True
    else:
        return False
    

def checkUserId(userId):
    conn = sqlite3.connect('telegramBot.db')
    cur = conn.cursor()

    cur.execute("""SELECT chatId FROM partecipantiBot """)
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
    fetch_chat_id = curs1.execute("""SELECT chatId FROM partecipantiBot """)
    chat_id_list = []

    for row in fetch_chat_id:
        i = 0
        chat_id_list.append(row[0])
        i = i + 1

    conn1.commit()
    conn1.close()
    
    return chat_id_list


def fromChatIdGetUser(chatId):
    conn = sqlite3.connect('telegramBot.db')
    curs = conn.cursor()
    curs.execute("""SELECT * FROM partecipantiBot""")
    fetch_chat_id = curs.fetchall
    conn.commit()
    conn.close	

    for row in fetch_chat_id:
        if chatId in row[1]:
            
            username = row[0]
            break

    return username        


def fromUserGetChatId(user):

    fetch_chat_id = getUserQuery()

    chat_id = 0
    for row in fetch_chat_id:
        if user in row[0]:
            
            chat_id = row[1]
            break       
    return chat_id 


def getUserQuery():
    conn1 = sqlite3.connect('telegramBot.db')
    curs1 = conn1.cursor()
    curs1.execute("""SELECT * FROM partecipantiBot """)
    fetch_chat_id = curs1.fetchall()
    conn1.commit()
    conn1.close
    return fetch_chat_id


def upgradeTeam(newTeam: str, chatId: int):
    conn1 = sqlite3.connect('telegramBot.db')
    curs1 = conn1.cursor()
    sql = f"UPDATE partecipantiBot SET squadra = '{newTeam.strip().lower()}' WHERE chatId = {chatId}"
    curs1.execute(sql)
    conn1.commit()
    conn1.close


def upgradeTuSaiChi(TuSaiChi: str, chatId: int):
    conn1 = sqlite3.connect('telegramBot.db')
    curs1 = conn1.cursor()

    if TuSaiChi.strip().lower() == 'si' or TuSaiChi.strip().lower() == 'sì':
        bool_tu_sai_chi = True
    else:
        bool_tu_sai_chi = False

    sql = f"UPDATE partecipantiBot SET tuSaiChi = '{bool_tu_sai_chi}' WHERE chatId = {chatId}"
    curs1.execute(sql)
    conn1.commit()
    conn1.close

    return bool_tu_sai_chi

def getChatIdMembersOfTeam( team: str):

    conn1 = sqlite3.connect('telegramBot.db')
    curs1 = conn1.cursor()
    sql = f"SELECT squadra,chatId FROM partecipantiBot "
    team_and_chat_id = curs1.execute(sql)
    conn1.commit()
    conn1.close

    chat_id_list = []
    
    for row in team_and_chat_id:
        if team in row:
            i = 0
            chat_id_list.append(row[1])
            i = i + 1

    conn1.commit()
    conn1.close()

    return chat_id_list

def fromChatIdGetTeam(chatId):
    fetch_chat_id = getUserQuery()
    
    for row in fetch_chat_id:
        if chatId == row[1]:
            
            team = row[2]
            break       
    return team