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
        users = getUserQuery()
        await context.bot.send_message(chat_id = 6307311132, text=(f'{users}'), parse_mode='HTML')

