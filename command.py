from DBexecution import CheckAddmin, checkUserId, getUserQuery


from telegram import Update
from telegram.ext import ContextTypes, CallbackContext


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    await context.bot.send_message(
        chat_id = chat_id,
        text=(f'Hello in this bot. Your chat id is:{chat_id}'), parse_mode='HTML'
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
   