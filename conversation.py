from telegram import Update
from telegram.ext import ContextTypes, CallbackContext, ConversationHandler

from DBexecution import ControlUser, checkUserId, CheckAddmin, fromChatIdGetUser, upgradeTeam, upgradeTuSaiChi,fromUserGetChatId

ANSWER,NOME,SQUADRA,TUSAICHI = range(4)

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
        await context.bot.send_message(chat_id=chat_id, text='Mi dispiace ma risulta che tu sia già registrato', parse_mode='HTML')
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
    chat_id = update.effective_chat.id
    tu_sai_chi = update.effective_message.text
    chat_id_user = fromUserGetChatId(newUsername)
    upgradeTuSaiChi(tu_sai_chi, chat_id_user)

    if tu_sai_chi in 'True':
        await context.bot.send_message(chat_id=chat_id_user, text='Sei il tuSaiChi !!!', parse_mode='HTML')
    else:
        await context.bot.send_message(chat_id=chat_id_user, text='Mi spiace ma non sei il tu sai chi\nrenditi comunque utile alla squadra aiutando il tuSaiChi', parse_mode='HTML')
    return  ConversationHandler.END
