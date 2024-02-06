from DBexecution import CheckAddmin, checkUserId, getUserQuery


from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    button = [KeyboardButton('start')]
    await context.bot.send_message(
        chat_id = chat_id,
        text=('Benvenuto a tuSaiChi un gioco che meterà a dura prova le tue abilità.\
              \nIl gioco non è semplice vi avviso. \
              L\'unico modo per vincere è facendo gioco di squadra ed aiutando il tuSaiChi della propria squadra a manifestarsi senza farsi scoprire.\nSe non hai mai giocato al questo gioco o le regole ti sono poco chiare non preoccuparti usa il comando /help.\
              \nUna volta che hai capito le regole e ti senti pronto per iniziare questa sfida clicca il comando /addme.\
              \nBuons fortuna e ricorda di non nominare mai tu sai chi'),reply_markup=ReplyKeyboardMarkup(button), parse_mode='HTML'
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
   
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    testo =   'tuSaiChi è un gioco a squadre dove la squadra che totalizza più punti alla fine della settimana vince.\n' \
              'Ogni squadra è composta da un tuSaiChi e da degli aiutanti.\n'\
              'Il tuSaiChi è il giocatore più importante della squadra ed è l\'unico che può interagire con il giudice supremo.\n'\
              'Lo scopo del gioco è quello di indovinare chi è il tuSaiChi delle altre squadre e non fare scoprire il prorpio tuSaiChi.\n'\
              'Ogni tuSaiChi sarà obbligato a manifestarsi giornalmente ovvero ad appendere in un luogo ed un orario prestabilito un foglio con le instruzioni che il giudice supremo gli impone.\n'\
              'Per prima cosa ogni squadra dovrà decidere un firma che rappresenterà l\'identità della squadra.\n'\
              'Attenzione non dovete dire a tutti i concorrenti che quella firma è della vostra squadra ma anzi sarà compito loro indovinarlo.\n'\
              'Alla sera il giudice supremo comunicherà al tuSaiChi il luogo dove appendere il manifesto e l\'orario in qui manifestarsi.\n'\
              '\bIMPORTANTE\n'\
              'Solo il tuSaiChi può manifestarsi nessun altro elemento della squadra può farlo.\n'\
              'Per più informazioni usate il comando /comemanifestarsi.\n'\
              'Con il passare del tempo i manifest saranno sempre più difficili e autodescrittive del tuSaiChi il tutto per rendere il gioco più....elettrizzante.\n'\
              'Ad ogni giorno che passa sará quindi più facile scoprire chi è il tuSaiChi delle altre squadre e pertanto il punteggio per la scoperta del tuSaiChi diminuirá.\n'\
              'Sempre alla sera si avrá la possibilità di accusare qualcuno per che sia il tuSaiChi. Attenzione solo un\'accusa per squadra può essere fatta.\n'\
              'Inoltre una persona accusata non può essere accusata due volte di seguito dalla stessa squadra perciò state attenti.\n'\
              'Perché l\'accusa dovete convincere il giudice supremo con prove suffiecienti altrimenti l\'accusato potrà essere ritenuto salvo e non accusabile il giorno dopo.\n'\
              'Durante la settimana ci saranno varie sfide da affrontare che vi daranno bonus o malus.\n'\
              'Per più informazioni sui punteggi usa il comando /punteggi.\n '\
              'Alla fine della settimana chi avrà il punteggio più alto vince.'
    
    await context.bot.send_message(
        chat_id = chat_id,
        text=(testo), parse_mode='HTML'
    )

     
     

    