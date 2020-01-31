import configparser
import logging
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

config_path = 'data.ini'
config = configparser.ConfigParser()
config.read(config_path)
TOKEN = config.get('bot_data', 'TOKEN')
REQUEST_KWARGS = {
    'proxy_url': 'http://14.162.145.116:46516/',
    # Optional, if you need authentication:
    # 'username': 'PROXY_USER',
    # 'password': 'PROXY_PASS',
}

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id, text='Holy moly! There is someone! Talk to me, please!')


updater = Updater(token=TOKEN, use_context=True, request_kwargs=REQUEST_KWARGS)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling(.5)
# import requests
#
# api-endpoint
# URL = ''.join(['https://api.telegram.org/bot', TOKEN, '/getupdates'])
#
# # location given here
#
# # sending get request and saving the response as response object
# r = requests.get(url=URL)
#
# # extracting data in json format
# data = r.json()
#
# # printing the output
# print(data)
