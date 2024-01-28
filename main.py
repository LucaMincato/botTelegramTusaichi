from telegram.ext import ApplicationBuilder, CommandHandler
from telegram.ext import filters, MessageHandler
from telegram.ext import ConversationHandler

from command import start, getPartecipant
from conversation import start_dialog, answer, cancel, ANSWER
from SecretToken import BOT_TOKEN

if __name__ == '__main__':
    
    application = ApplicationBuilder().token(BOT_TOKEN).build()

   # startdialog_handler = CommandHandler('start_dialog', start_dialog)
    start_handler = CommandHandler('start', start) 
    list_handler = CommandHandler('getPartecipant', getPartecipant) 
   
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start_dialog',start_dialog)],
        states={
            ANSWER: [MessageHandler(filters.TEXT,answer),
                     CommandHandler('cancel',cancel)],

        },
        fallbacks=[CommandHandler('cancel',cancel)],
    )

    application.add_handler(start_handler)
    application.add_handler(conv_handler)
    application.add_handler(list_handler)


    application.run_polling()
    