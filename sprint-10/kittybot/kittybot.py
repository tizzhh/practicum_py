from telegram import Bot
from telegram.ext import CommandHandler, Updater, Filters, MessageHandler


TELEGRAM_TOKEN = '6722886196:AAFvxWXiBI4Sf2HVKKo3LP4dPXMHvzV0XxI'
CHAT_ID = '430814010'

bot = Bot(token=TELEGRAM_TOKEN)
updater = Updater(token=TELEGRAM_TOKEN)


def send_message(message):
    bot.send_message(CHAT_ID, message)


def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Privetuli')


def wake_up(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Thanks, I am awake now')


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
updater.start_polling()
updater.idle()