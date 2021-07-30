import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters

#Obtener la info de la sesion
logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


#FUNCIONES DE LOS COMANDOS
def start(update, context):
    update.message.reply_text("Hola perro")
    botones0(update)

#FUNCION BOTONES
def botones0(update):
    btn1 = InlineKeyboardButton(text = 'Airdrop', callback_data = 'airdrop')
    update.message.reply_text(
        text = 'heyyy',
        reply_markup = InlineKeyboardMarkup([
        [btn1]
        ]
        )
    )

updater = Updater("1899599200:AAEkbuuuoytTKpTyiuiTdggO3_ycLUUaEOs", use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

#estados de conversation
dp.add_handler(ConversationHandler(
    entry_points = [
        CallbackQueryHandler(pattern = 'airdrop', callback= 'airdrop')
    ],
    states = {},
    fallbacks = []
))


updater.start_polling()
updater.idle()