from telegram.ext import ApplicationBuilder, CommandHandler
from telegram.ext import filters, MessageHandler
from telegram.ext import ConversationHandler
from PyDictionary import PyDictionary

from command import start

from conversation import 

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    dictionary = PyDictionary()


    application.bot_data['dictionary'] = dictionary


    start_handler = CommandHandler('start', start)
    meaning_handler = CommandHandler('mean', meaning)


    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start_dialog',start_dialog)],
        states={
            ANSWER: [MessageHandler(filters.Regex('(Yes)$'),answer)],
            ANSWER2: [MessageHandler(filters.Regex('(Yes|no)$'),answer)],
            ANSWER3: [MessageHandler(filters.Regex('(Yes)$'),answer)],
            ANSWER4: [MessageHandler(filters.Regex('(Yes)$'),answer)],
            ANSWER5: [MessageHandler(filters.Regex('(Yes)$'),answer)],
        },
        fallbacks=[CommandHandler('cancel',cancel)],
    )

    application.add_handler(start_handler)
    application.add_handler(meaning_handler)
    application.add_handler(conv_handler)


    application.run_polling()
