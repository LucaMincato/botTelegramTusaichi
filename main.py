from telegram.ext import ApplicationBuilder, CommandHandler
from telegram.ext import filters, MessageHandler
from telegram.ext import ConversationHandler
from PyDictionary import PyDictionary

from command import start

from conversation import 

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    startdialog_handler = CommandHandler('start_dialog', start_dialog)
    start_handler = CommandHandler('start', start) 
   
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start_dialog',start_dialog)],
        states={
            ANSWER: [MessageHandler(filters.TEXT,answer),
                     CommandHandler('cancel',cancel)],

        },
        fallbacks=[CommandHandler('cancel',cancel)],
    )

    application.add_handler(start_handler)
    application.add_handler(startdialog_handler)
    application.run_polling()
