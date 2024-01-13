import logging
import os

import requests
from dotenv import load_dotenv
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext, CommandHandler, Updater

load_dotenv()
secret_token = os.getenv('TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)


URL = 'https://api.thecatapi.com/v1/images/search'


def get_new_cat_img():
    try:
        response = requests.get(URL).json()
    except Exception as e:
        logging.error(f'Error with main API interaction: {e}')
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url).json()
    return response[0].get('url')


def new_cat(update: Update, context: CallbackContext):
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_cat_img())


def wake_up(update: Update, context: CallbackContext):
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['/newcat']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text=f'Thanks, {chat.first_name} I am awake now',
        reply_markup=button,
    )
    context.bot.send_photo(chat.id, get_new_cat_img())


def main():
    updater = Updater(token=secret_token)
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
