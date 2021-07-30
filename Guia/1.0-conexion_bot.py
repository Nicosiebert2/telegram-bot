import logging
from telegram.ext import Updater


#Obtener la info de la sesion
logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#logger = logging.getLogger() # no se si haga falta el logger

#definimos el updater donde volcamos el token
updater = Updater("1899599200:AAEkbuuuoytTKpTyiuiTdggO3_ycLUUaEOs", use_context=True)

#start_polling para mantener la conexino
updater.start_polling()

#idle para poder cerrar la conexion
updater.idle()