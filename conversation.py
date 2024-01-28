from telegram import Update
from telegram.ext import ContextTypes, CallbackContext, ConversationHandler

from DBexecution import ControlUser

ANSWER,ANSWER1 = range(2)

def registerId():
    global userId
    global user
    content = (user,str(userId))
    return content


async def start_dialog(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text='Benvenuto a tu sai chi il gioco che ti metterà alla prova\nInserisci il tuo nome', parse_mode='HTML')
    return ANSWER



async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global userId
    global user
    chat_id = update.effective_chat.id
    print( chat_id)
    userId = chat_id
    user = update.effective_message.text
    entrydb = registerId()
    already_exist = ControlUser(entrydb)

    if already_exist:
        await context.bot.send_message(chat_id=chat_id, text='Mi dispiace ma risulta che tu sia già registrato', parse_mode='HTML')
    else:
        await context.bot.send_message(chat_id=chat_id, text='Complimenti sei stato aggiunto ai partecipanti', parse_mode='HTML')
        
    return ConversationHandler.END



async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text='operazione fallita', parse_mode='HTML')
    return ConversationHandler.END





