from telegram import Bot


TELEGRAM_TOKEN = '6722886196:AAFvxWXiBI4Sf2HVKKo3LP4dPXMHvzV0XxI'
CHAT_ID = '430814010'

bot = Bot(token=TELEGRAM_TOKEN)


def send_message(message):
    bot.send_message(CHAT_ID, message)


send_message('test framework, hello')