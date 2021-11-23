from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from random import seed, randint
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
        
def pic(update: Update, context: CallbackContext):
    seed(1)
    
    if(context.args[0] == "cat"):
        photo_ls = ["https://steemitimages.com/640x0/https://img.esteem.ws/5e0zyxfznd.jpg", "https://filmdaily.co/wp-content/uploads/2020/04/cute-cat-videos-lede-1300x882.jpg", "https://preview.redd.it/zn5l96e3jyx71.jpg?width=690&format=pjpg&auto=webp&s=f7de38277a19d48a0f562a9c668ee81973f15844", "https://www.baldivisvet.com.au/wp-content/uploads/2017/10/cats-cute-cat-licking-paw1920.jpg", "https://i.guim.co.uk/img/media/43352be36da0eb156e8551d775a57fadba8ae6d7/0_0_1440_864/master/1440.jpg?width=620&quality=85&auto=format&fit=max&s=b68713c76b3d7fc98eaba7d9065f97da"]
        
        value = randint(0, 4)
        
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_ls[value], caption="Here is a cute cat for you :)")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="It's not cute enough :(")    
    
def echo(update: Update, context: CallbackContext):
    if(update.message.text == "siapa yang ganteng?"):
        context.bot.send_message(chat_id=update.effective_chat.id, text="anda tentunya.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
pic_handler = CommandHandler('pic', pic)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(pic_handler)

updater.start_polling()