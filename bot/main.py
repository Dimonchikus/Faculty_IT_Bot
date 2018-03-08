import telebot
from bot import bussines
from bot import constants

Bot = telebot.TeleBot(constants.token_of_bot)

@bussines.Bot.message_handler(commands=['start'])
def handle_start(message):
    bussines.start(message)


@bussines.Bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "'Відмітка про перебування поза межами інституту":
        Bot.send_message(message.from_user.id, 'Введіть ПБІ')
    elif message.text == "Сповістити про зауваження чи загрозу":
        Bot.send_message(message.from_user.id, 'Опишіть стан дій')

try:
    b = bussines.Bot.polling(none_stop=True, interval=0)
    print(b)
except ConnectionError:
    print("Aborted Connection")



