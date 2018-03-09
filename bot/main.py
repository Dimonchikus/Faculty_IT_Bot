import telebot
import requests
import json
from telebot.types import Location

from bot import bussines
from bot import constants

bussines.Bot = telebot.TeleBot(constants.token_of_bot)


@bussines.Bot.message_handler(commands=['start'])
def handle_start(message):
    bussines.start(message)


@bussines.Bot.message_handler(content_types=['text'])
def handle_text(message):
    if bussines.start_flag:
        bussines.add_cadet(message)
    elif message.text == "Відмітка про перебування поза межами інституту":
        bussines.Bot.send_message(message.from_user.id, 'Ви відмічені')
    elif message.text == "Сповістити про зауваження чи загрозу":
        bussines.Bot.send_message(message.from_user.id,
                                  'Опишіть коротко, що трапилося. За можливості пришліть своє місцезнаходження')
        bussines.if_alert = True


@bussines.Bot.message_handler(content_types=["location"])
def get_location(message):
    bussines.get_location(message)


try:
    b = bussines.Bot.polling(none_stop=True, interval=0)
    print(b)
except ConnectionError:
    print("Aborted Connection")
