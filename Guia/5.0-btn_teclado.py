#Documentacion
#  https://python-telegram-bot.readthedocs.io
#  https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html
#  https://python-telegram-bot.readthedocs.io/en/stable/telegram.keyboardbutton.html


#Librerias
import logging # Login
from telegram import KeyboardButton, ReplyKeyboardMarkup #Teclado
from telegram.ext import Updater, CommandHandler #Token y comandos

#Obtener la info de la sesion
logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger()


#Funcion Start
def start(update, context):
    btn_teclado(update, context)

    
# Definimos los botones y sus respectivos nombres
def btn_teclado(update, context):
    btn1 = KeyboardButton(text="boton1")
    btn2 = KeyboardButton(text="boton2")
    btn3 = KeyboardButton(text="boton3")
    btn4 = KeyboardButton(text="boton4")
    
    #llamamos a la funcion para mostrar los botones
    mostrar_botones(update, btn1, btn2, btn3, btn4)


#Funcion para mostrar Botones
def mostrar_botones(update, btn1, btn2, btn3, btn4):
    update.message.reply_text(
        text= "estos son los botones",
        reply_markup= ReplyKeyboardMarkup(
            keyboard= [[btn1, btn2], [btn3, btn4]],
            one_time_keyboard=True,  #Ocultar los botones una vez presionado el boton
            resize_keyboard=True #redimensionar
        )
    )

#para enlazar el token y añadir comandos

updater = Updater("Tu token")

#Comandos
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

#Mantener y poder terminar la sesion
updater.start_polling()
updater.idle()
