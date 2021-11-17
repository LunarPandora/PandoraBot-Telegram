from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
import json

# import logging
# logging.basicConfig(format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token = '2139371345:AAFiOE7uD1T5Cwn9X84YXFXoMXp4dMPhkvc', use_context=True)
dispatcher = updater.dispatcher
x = 0

def start(update: Update, context: CallbackContext):
    global x
    resp_arr = ["Hello! My name is Pandora!", "Uh, hello?", "Hello there! I can hear you!", "I am here!", "Really?"]
    
    if x < 5:
        context.bot.send_message(chat_id=update.effective_chat.id, text=resp_arr[x])
        x += 1
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="...")
        x += 1
    
def echo(update: Update, context: CallbackContext):
    if(update.message.text == "siapa yang ganteng?"):
        context.bot.send_message(chat_id=update.effective_chat.id, text="anda tentunya.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()