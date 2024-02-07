from telegram.ext import ApplicationBuilder, CommandHandler
from telegram.ext import filters, MessageHandler
from telegram.ext import ConversationHandler

from command import start, getPartecipant, help,comemanifestarsi, punteggi
from conversation import start_dialog, answer, cancel, endSendMessageToEveryone, startSendMessageToEveryone, startSendMessageToYourTeam, endSendMessageToYourTeam
from conversation import startAdminInsertPartecipant, teamAdminInsertPartecipant, tuSaiChiAdminInsertPartecipant, endAdminInsertPartecipant, sendPhotoToEveryone,BeReal, endBeReal
from conversation import ANSWER, MESSAGE_TO_EVERYONE, NOME, SQUADRA, TUSAICHI, MESSAGE_TO_TEAM, BEREAL_TO_EVERYONE
from SecretToken import BOT_TOKEN

if __name__ == '__main__':
    
    application = ApplicationBuilder().token(BOT_TOKEN).build()

   # startdialog_handler = CommandHandler('start_dialog', start_dialog)
    start_handler = CommandHandler('start', start) 
    list_handler = CommandHandler('lista_partecipanti', getPartecipant) 
    help_handler = CommandHandler('help', help) 
    help_manifesto_handler = CommandHandler('come_manifestarsi',comemanifestarsi)
    help_punteggi_handler =  CommandHandler('punteggi',punteggi)
   
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('addme',start_dialog)],
        states={
            ANSWER: [MessageHandler(filters.TEXT & (~filters.COMMAND),answer),
                     CommandHandler('cancel',cancel)],

        },
        fallbacks=[CommandHandler('cancel',cancel)],
    )

    conv_assign_partecipant_handler = ConversationHandler(
    entry_points=[CommandHandler('aggiungi_partecipanti',startAdminInsertPartecipant)],
    states={
        NOME: [MessageHandler(filters.TEXT  & (~filters.COMMAND),teamAdminInsertPartecipant),
                 CommandHandler('cancel',cancel)],
        SQUADRA: [MessageHandler(filters.TEXT & (~filters.COMMAND),tuSaiChiAdminInsertPartecipant),
                 CommandHandler('cancel',cancel)],
        TUSAICHI: [MessageHandler(filters.TEXT & (~filters.COMMAND),endAdminInsertPartecipant),
                 CommandHandler('cancel',cancel)],
    },
        fallbacks=[CommandHandler('cancel',cancel)],
    )

    conv_to_all_handler = ConversationHandler(
    entry_points=[CommandHandler('messageToAll',startSendMessageToEveryone)],
    states={
        MESSAGE_TO_EVERYONE: [MessageHandler(filters.TEXT,endSendMessageToEveryone),
                              CommandHandler('cancel',cancel)],

    },
        fallbacks=[CommandHandler('cancel',cancel)],
    )

    conv_to_team_handler = ConversationHandler(
    entry_points=[CommandHandler('messageToTeam',startSendMessageToYourTeam)],
    states={
        MESSAGE_TO_TEAM: [MessageHandler(filters.TEXT,endSendMessageToYourTeam),
                              CommandHandler('cancel',cancel)],

    },
        fallbacks=[CommandHandler('cancel',cancel)],
    )


    beReal_handler = ConversationHandler(
    entry_points=[CommandHandler('BeReal',BeReal)],
    states={
            BEREAL_TO_EVERYONE: [MessageHandler(filters.PHOTO & (~filters.FORWARDED) & (~filters.COMMAND) & (~filters.TEXT),endBeReal),
                                 CommandHandler('cancel',cancel)],

        },
        fallbacks=[CommandHandler('cancel',cancel)],
    )


    application.add_handler(start_handler)
    application.add_handler(conv_handler)
    application.add_handler(list_handler)
    application.add_handler(conv_assign_partecipant_handler)
    application.add_handler(help_handler)
    application.add_handler(conv_to_all_handler)
    application.add_handler(conv_to_team_handler)
    application.add_handler(beReal_handler)
    application.add_handler(help_manifesto_handler)
    application.add_handler(help_punteggi_handler)

    application.run_polling()
    