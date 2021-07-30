import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup#botones
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

#Obtener la info de la sesion
logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger()


#FUNCIONES DE LOS COMANDOS
def start(update, context):
    update.message.reply_text("Hola perro")
    botones0(update)

#FUNCION BOTONES
def botones0(update):
    #definir los botones
    btn1 = InlineKeyboardButton(text = 'Airdrop', callback_data = 'airdrop')
    update.message.reply_text(
        text = 'heyyy',
        reply_markup = InlineKeyboardMarkup([
        [btn1]
        ]
        )
    )
    #definimos el callback del messge query
def airdrop(update):
    update.message.reply_text("hola")
    return #Al estado
    
#variable dispatcher
updater = Updater("1899599200:AAEkbuuuoytTKpTyiuiTdggO3_ycLUUaEOs", use_context=True)
dp = updater.dispatcher

#Comandos
dp.add_handler(CommandHandler("start", start))

#enlazar el callback_data al callback

dp.add_handler(CallbackQueryHandler(pattern = 'airdrop', callback= airdrop))# el callback va como funcion

#botones




updater.start_polling()
updater.idle()