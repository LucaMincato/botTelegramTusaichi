import json
import logging
from typing import Union, Dict, List


from telegram import Update
from telegram.ext import ContextTypes, CallbackContext


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    await context.bot.send_message(
        chat_id = chat_id,
        text=(f'Hello in this bot. Your chat id is:{chat_id}'), parse_mode='HTML'
    )


