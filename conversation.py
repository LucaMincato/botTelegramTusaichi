from telegram import Update
from telegram.ext import ContextTypes, CallbackContext, ConversationHandler
import time

from DBexecution import ControlUser, checkUserId, CheckAddmin, upgradeTeam, getTuSaiChi
from DBexecution import  upgradeTuSaiChi, fromUserGetChatId, fetchDbChatId, fromChatIdGetTeam, getChatIdMembersOfTeam

ANSWER,NOME,SQUADRA,TUSAICHI, MESSAGE_TO_EVERYONE, MESSAGE_TO_TEAM,TUSAICHI_VERDE,TUSAICHI_BLU,TUSAICHI_GIALLO,TUSAICHI_ROSSO,PHOTO_SPOTTED,TEXT_SPOTTED = range(12)


def registerId():
    global userId
    global user
    content = (user,userId)
    return content



async def start_dialog(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text='Benvenuto a tu sai chi il gioco che ti metterà alla prova\nInserisci il tuo nome', parse_mode='HTML')
    return ANSWER



async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global userId
    global user
    chat_id = update.effective_chat.id
    userId = chat_id
    user = update.effective_message.text
    entrydb = registerId()
    already_exist = ControlUser(entrydb)

    if already_exist:
        await context.bot.send_message(chat_id=chat_id, text='C\'è stato un errore.\nTi sei già registrato.', parse_mode='HTML')
        await context.bot.send_message(chat_id=6307311132, text=f'Luca {user} sta sercando di registrarsi due volte', parse_mode='HTML')
    else:
        await context.bot.send_message(chat_id=chat_id, text='Complimenti sei stato aggiunto ai partecipanti.\nOra aspetta che admin ti inserisca in una squadra e ti dica se sei il tuSaiChi', parse_mode='HTML')
        await context.bot.send_message(chat_id=6307311132, text=f'Luca {user} vorrebbe registrarsi assegnali una squadra e rendilo o meno il tuSaiChi', parse_mode='HTML')
        
    return ConversationHandler.END



async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text='operazione fallita', parse_mode='HTML')
    return ConversationHandler.END



async def startAdminInsertPartecipant(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    is_it_admin = CheckAddmin(chat_id)

    if is_it_admin:
        
        await context.bot.send_message(chat_id=chat_id, text='Inserisci il nome della persona che vuoi aggiungere', parse_mode='HTML')
    else:
         await context.bot.send_message(chat_id=chat_id, text='Mi dispiace ma solo Luca Può usare questo comando', parse_mode='HTML')

    return NOME



async def teamAdminInsertPartecipant(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    global newUsername
    newUsername = update.effective_message.text
    chat_id_user = fromUserGetChatId(newUsername)

    if 0 != chat_id_user:

        checkUserId(chat_id_user)   
        await context.bot.send_message(chat_id=chat_id, text=f'Luca a che squadra vuoi assegnare {newUsername}?\nGiallo\bRosso\bBlu\bVerde', parse_mode='HTML')
        return SQUADRA
    else:

        await context.bot.send_message(chat_id=chat_id, text='Luca questo nome non esiste', parse_mode='HTML')
        return  ConversationHandler.END
    


async def tuSaiChiAdminInsertPartecipant(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    squadra = update.effective_message.text
    chat_id_user = fromUserGetChatId(newUsername)
    upgradeTeam(squadra, chat_id_user)

    if squadra.strip().lower() in ['giallo', 'verde', 'rosso','blu']:
        await context.bot.send_message(chat_id=chat_id, text=f'Vuoi che sia il tuSaiChi', parse_mode='HTML')
        await context.bot.send_message(chat_id=chat_id_user, text=f'Sei stato assegnato alla squadra {squadra}', parse_mode='HTML')
        return TUSAICHI
    else:
        await context.bot.send_message(chat_id=chat_id, text='La squadra non esiste', parse_mode='HTML')
        return  ConversationHandler.END
    


async def endAdminInsertPartecipant(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    tu_sai_chi = update.effective_message.text
    chat_id_user = fromUserGetChatId(newUsername)
    bool_tu_sai_chi = upgradeTuSaiChi(tu_sai_chi, chat_id_user)

    if bool_tu_sai_chi:

        await context.bot.send_message(chat_id=chat_id_user, text='Sei il tuSaiChi !!!', parse_mode='HTML')
    else:
        await context.bot.send_message(chat_id=chat_id_user, text='Mi spiace ma non sei il tu sai chi\nrenditi comunque utile alla squadra aiutando il tuSaiChi', parse_mode='HTML')
    
    return  ConversationHandler.END



async def startSendMessageToEveryone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    is_it_admin = CheckAddmin(chat_id)
    
    if is_it_admin:
        
        await context.bot.send_message(chat_id=chat_id, text='Che messaggio vuoi mandare a tutti?', parse_mode='HTML')
    else:
         await context.bot.send_message(chat_id=chat_id, text='Mi dispiace ma solo Luca Può usare questo comando', parse_mode='HTML')

    return MESSAGE_TO_EVERYONE



async def endSendMessageToEveryone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text_to_send = update.effective_message.text
    users_chat_id = fetchDbChatId()

    for row in users_chat_id:
        
        await context.bot.send_message(chat_id= row, text= text_to_send, parse_mode='HTML')
       
    return  ConversationHandler.END



async def startSendMessageToYourTeam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    await context.bot.send_message(chat_id=chat_id, text='Che messaggio vuoi mandare al tuo team?', parse_mode='HTML')
   
    return MESSAGE_TO_TEAM



async def endSendMessageToYourTeam(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    text_to_send = update.effective_message.text
    users_chat_id = fetchDbChatId()
    team = fromChatIdGetTeam(chat_id)
    users_chat_id = getChatIdMembersOfTeam(team)

    for row in users_chat_id:
        await context.bot.send_message(chat_id= row, text= text_to_send, parse_mode='HTML')

    return  ConversationHandler.END


async def startMessageTuSaiChi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    is_it_admin = CheckAddmin(chat_id)

    if is_it_admin:
        await context.bot.send_message(chat_id=chat_id, text='Scrivi il manifesto per la squadra gialla', parse_mode='HTML')
        return TUSAICHI_GIALLO
    else:
         await context.bot.send_message(chat_id=chat_id, text='Mi dispiace ma solo Luca Può usare questo comando', parse_mode='HTML')
         return  ConversationHandler.END


async def yellowMessageTuSaiChi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text_to_send = update.effective_message.text
    team = 'giallo'
    yellow_tusaichi_chat_id = getTuSaiChi(team)

    await context.bot.send_message(chat_id=yellow_tusaichi_chat_id, text=text_to_send, parse_mode='HTML')
    await context.bot.send_message(chat_id=chat_id, text='Scrivi il manifesto per la squadra rossa', parse_mode='HTML')
    return TUSAICHI_ROSSO


async def redMessageTuSaiChi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text_to_send = update.effective_message.text
    team = 'rosso'
    yellow_tusaichi_chat_id = getTuSaiChi(team)

    await context.bot.send_message(chat_id=yellow_tusaichi_chat_id, text=text_to_send, parse_mode='HTML')
    await context.bot.send_message(chat_id=chat_id, text='Scrivi il manifesto per la squadra blu', parse_mode='HTML')
    return TUSAICHI_BLU



async def blueMessageTuSaiChi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text_to_send = update.effective_message.text
    team = 'blu'
    yellow_tusaichi_chat_id = getTuSaiChi(team)

    await context.bot.send_message(chat_id=yellow_tusaichi_chat_id, text=text_to_send, parse_mode='HTML')
    await context.bot.send_message(chat_id=chat_id, text='Scrivi il manifesto per la squadra verde', parse_mode='HTML')
    return TUSAICHI_VERDE


async def greenMessageTuSaiChi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text_to_send = update.effective_message.text
    team = 'verde'
    yellow_tusaichi_chat_id = getTuSaiChi(team)

    await context.bot.send_message(chat_id=yellow_tusaichi_chat_id, text=text_to_send, parse_mode='HTML')
    await context.bot.send_message(chat_id=chat_id, text='Hai mandato tutti i manfesti', parse_mode='HTML')
    return  ConversationHandler.END



async def startSpotted(update: Update, context: ContextTypes.DEFAULT_TYPE):

    """photo received management"""

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="manda una foto di che cosa hai visto"
    )
    return PHOTO_SPOTTED


async def photoSpotted(update: Update, context: ContextTypes.DEFAULT_TYPE):

    """photo received management"""
    chat_id = update.effective_chat.id
    users_chat_id = fetchDbChatId()
    team = fromChatIdGetTeam(chat_id)
    users_chat_id = getChatIdMembersOfTeam(team)
    users_chat_id.append(6307311132)
    users_chat_id.remove(chat_id)
    seconds = time.time()
    local_time = time.ctime(seconds)

    for row in users_chat_id:
        await context.bot.send_photo(
            chat_id=row, photo=update.message.photo[-1].file_id
        )

        await context.bot.send_message(
        chat_id=row, text=f"{local_time}"
        )

    await context.bot.send_message(chat_id=chat_id, text="aggiungi una descrizione")
        
    return TEXT_SPOTTED


async def textSpotted(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text_to_send = update.effective_message.text
    users_chat_id = fetchDbChatId()
    team = fromChatIdGetTeam(chat_id)
    users_chat_id = getChatIdMembersOfTeam(team)
    users_chat_id.append(6307311132)
    users_chat_id.remove(chat_id)

    
    for row in users_chat_id:
        await context.bot.send_message(chat_id= row, text= text_to_send, parse_mode='HTML')

    await context.bot.send_message(chat_id= chat_id, text= "lo spotted è andato a buon fine", parse_mode='HTML')

    return  ConversationHandler.END