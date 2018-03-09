import telebot

from bot import bussines
from bot import constants

bussines.Bot = telebot.TeleBot(constants.token_of_bot)


@bussines.Bot.message_handler(commands=['start'])
def handle_start(message):
    with open('bd.txt', encoding='utf-8') as fio:
        constants.db = fio.readlines()
    """
    start working with @miti_faculty_it_bot
    message == '/start'
    :param message:
    :return:
    """
    bussines.start(message)


@bussines.Bot.message_handler(content_types=['text'])
def handle_text(message):
    """
    processing of text queries
    :param message:
    :return:
    """
    if bussines.start_flag:
        """
        add cadet data to database
        """
        bussines.add_cadet(message)

    elif message.text == "Відмітка про перебування поза межами інституту":
        """
        certificate of stay outside the institute
        """
        bussines.Bot.send_message(message.from_user.id, 'Надішліть ваші геодані')
        bussines.location = True

    elif message.text == "Сповістити про зауваження чи загрозу":
        """
        notice of warning or threat
        """
        bussines.Bot.send_message(message.from_user.id,
                                  'Опишіть коротко, що трапилося. За можливості пришліть своє місцезнаходження')
        bussines.if_alert = True

    elif bussines.if_alert:
        bussines.message_alert(message)


@bussines.Bot.message_handler(content_types=["location"])
def get_location(message):
    bussines.get_location(message)


try:
    b = bussines.Bot.polling(none_stop=True, interval=0)
    print(b)
except ConnectionError:
    print("Aborted Connection")
