import telebot
import requests
import json
from telebot.types import Location

from bot import bussines
from bot import constants

bussines.Bot = telebot.TeleBot(constants.token_of_bot)
if_alert = False;


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
        global if_alert
        if_alert = True;


@bussines.Bot.message_handler(content_types=["location"])
def get_location(message):
    global if_alert
    if (if_alert == True):
        r = requests.get(constants.google_map_url + str(message.location.latitude) + ',' + str(message.location.longitude) + constants.google_map_url_2)
        j = r.json()
        print(j)
        print("Done")
        bussines.Bot.send_location(message.from_user.id, message.location.latitude, message.location.longitude)

        if_alert = False


try:
    b = bussines.Bot.polling(none_stop=True, interval=0)
    print(b)
except ConnectionError:
    print("Aborted Connection")
