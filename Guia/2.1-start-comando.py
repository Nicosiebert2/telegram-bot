import logging
from telegram.ext import Updater, CommandHandler


logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
updater = Updater("1899599200:AAEkbuuuoytTKpTyiuiTdggO3_ycLUUaEOs", use_context=True)
logger = logging.getLogger() # no se si haga falta el logger


def start(update, context):
    update.message.reply_text("Hola perro")



#definimos nuestra variable para usar el dispatcher

dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start)) #comando y funcion del comando


#1.01
updater.start_polling()
updater.idle()