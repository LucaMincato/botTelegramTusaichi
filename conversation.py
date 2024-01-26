from telegram import Update
from telegram.ext import ContextTypes, CallbackContext, ConversationHandler

from DBexecution import ControlUser

ANSWER,ANSWER1 = range(2)

async def registerId():
    global userId
    global user
    content = (user,str(userId))
    return content


async def start_dialog(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text='Benvenuto a tu sai chi il gioco che ti metterà alla prova\n Inserisci il tuo nome', parse_mode='HTML')
    return ANSWER



async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global userId
    global user
    chat_id = update.effective_chat.id
    userId = chat_id
    user = update.effective_message.text
    entrydb = registerId()
    already_exist = ControlUser(entrydb)
    if already_exist == 0:
        context.bot.send_message(chat_id=chat_id, text='Mi dispiace ma risulta che tu sia già registrato', parse_mode='HTML')
    else:
        context.bot.send_message(chat_id=chat_id, text='Complimenti sei stato aggiunto ai partecipanti', parse_mode='HTML')
    return ConversationHandler.END



async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text='operazione fallita', parse_mode='HTML')
    return ConversationHandler.END




