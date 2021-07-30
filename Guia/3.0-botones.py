import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup#botones
from telegram.ext import Updater, CommandHandler

#Obtener la info de la sesion
logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger()

def start(update, context):
    update.message.reply_text("Hola perro")
    botones0(update)

def airdrop():
    pass
def buy():
    pass
def website():
    pass

#FUNCION BOTONES
def botones0(update):
    #definir los botones
    btn1 = InlineKeyboardButton(
        text = 'website', url = 'obixprueba.260mb.com'
    )
    #llamar a los botones
    update.message.reply_text(
        text = 'heyyy',
        reply_markup = InlineKeyboardMarkup([
            [btn1]
        ])
    )


updater = Updater("1899599200:AAEkbuuuoytTKpTyiuiTdggO3_ycLUUaEOs", use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("website", website))
updater.start_polling()
updater.idle()