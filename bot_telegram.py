#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from telegram.ext import *
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bot_token = ''

updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    first_name = update.message.from_user.first_name
    msg = 'Hola {} bienvenid@ hay los siguientes opciones /foto /argumentos'.format(first_name)
    context.bot.sendMessage(chat_id=update.message.chat_id, text=msg)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)    

def argumentos(update, context):
    args = context.args
    if len(args) > 0:
        msg = str(args)
    else: msg = 'debes de dar algun argumento'
    
    context.bot.sendMessage(chat_id=update.message.chat_id, text=msg)          

start_handler = CommandHandler('argumentos', argumentos)
dispatcher.add_handler(start_handler)

def foto(update, context):
    first_name = update.message.from_user.first_name
    with open('corazon.jpg', 'rb') as photo_file:
        context.bot.sendPhoto(chat_id=update.message.chat_id, photo=photo_file, \
            caption='Te amo {}'.format(first_name))    
            
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)           

start_handler = CommandHandler('foto', foto)
dispatcher.add_handler(start_handler)
updater.dispatcher.add_error_handler(error)
updater.start_polling()



    
