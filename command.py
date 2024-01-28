from DBexecution import CheckAddmin, checkUserId, getUserQuery


from telegram import Update
from telegram.ext import ContextTypes, CallbackContext


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    await context.bot.send_message(
        chat_id = chat_id,
        text=('Benvenuto a tuSaiChi un gioco che meterà a dura prova le tue abilità.\
              \nIl gioco non è semplice vi avviso. \
              L\'unico modo per vincere è facendo gioco di squadra ed aiutando il tuSaiChi della propria squadra a manifestarsi senza farsi scoprire.\nSe non hai mai giocato al questo gioco o le regole ti sono poco chiare non preoccuparti usa il comando /help.\
              \nUna volta che hai capito le regole e ti senti pronto per iniziare questa sfida clicca il comando /addme.\
              \nBuons fortuna e ricorda di non nominare mai tu sai chi'), parse_mode='HTML'
    )

async def getPartecipant(update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        is_it_admin = CheckAddmin(chat_id)
        users = getUserQuery()
        if is_it_admin:
            await context.bot.send_message(chat_id = 6307311132, text=('Username, chatId, Squadra, tuSaiChi'), parse_mode='HTML')
            for row in users:
                await context.bot.send_message(chat_id = 6307311132, text=(f'{row}\n'), parse_mode='HTML')
        else:
            await context.bot.send_message(chat_id=chat_id, text='Mi dispiace ma solo Luca Può usare questo comando', parse_mode='HTML')
   