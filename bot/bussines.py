import telebot
from bot import constants
import re
import requests
from time import gmtime, strftime

Bot = None

start_flag = False
if_alert = False
location = False


def start(message):
    """
    registration
    :param message:
    :return:
    """
    global Bot
    global start_flag
    Bot.send_message(message.from_user.id,
                     'Введіть дані (українською):\n'
                     '(Прізвище_Ім\'я_По батькові_Група_Номер телефону)\n'
                     'Зразок: Шкіцький_Володимир_Володимирович_265_+380951234567')
    start_flag = True
    print('start')


def check_for_correct(text):
    data = text.split('_')
    flag = False
    if data[0].isalpha() and re.match(r'^[А-Я,І,і]', data[0]):
        if data[1].isalpha() and re.match(r'^[А-Я,І,і]', data[1]):
            if data[2].isalpha() and re.match(r'^[А-Я,І,і]', data[2]):
                if data[3].isdigit() and data[3].__len__() == 3:
                    if re.match(r'^\+380[5,6,7,9][0-9]{8}$', data[4]):
                        flag = True
    return flag


def add_cadet(message):
    """
    add cadet data to database
    :param message:
    :return:
    """
    global start_flag

    for id_c in constants.db:
        if str(message.from_user.id) == (str(id_c).split())[0]:
            Bot.send_message(message.from_user.id, 'Ви вже додані до бази данихб як:\n' + ((str(id_c).split())[1]))
            start_flag = False
            return

    with open('bd.txt', 'a', encoding='utf-8') as fio:
        if check_for_correct(str(message.text)):
            fio.write(str(message.from_user.id) + ' ' + str(message.text) + '\n')
            user_markup = telebot.types.ReplyKeyboardMarkup(True)
            user_markup.row('Відмітка про перебування поза межами інституту', 'Сповістити про зауваження чи загрозу')
            Bot.send_message(message.from_user.id, 'Вас успішно занесено до бази даних', reply_markup=user_markup)
            start_flag = False
        else:
            Bot.send_message(message.from_user.id, "Введіть інформацію за поданим зразком")


def get_location(message):
    global if_alert
    global location
    r = requests.get(constants.google_map_url + str(message.location.latitude) + ',' + str(
        message.location.longitude) + constants.google_map_url_2)
    j = r.json()
    s = ''
    for i in (range(8))[::-1]:
        try:
            s += (str(j['results'][0]['address_components'][i]['long_name']) + ' ')
        except IndexError:
            s += ''
    if if_alert:
        with open('alert.txt', 'a', encoding='utf-8') as fio:
            fio.write(str(message.from_user.id) + '__-__' + s + ' | ' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + '\n')
        print("Done")
        Bot.send_message(message.from_user.id, "Done")
        if_alert = False
    if location:
        with open('location.txt', 'a', encoding='utf-8') as fio:
            fio.write(str(message.from_user.id) + '__-__' + s + ' | ' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + '\n')
        print("Done")
        Bot.send_message(message.from_user.id, "Done")
        location = False


def message_alert(message):
    global if_alert

    with open('alert_message.txt', 'a', encoding='utf-8') as fio:
        fio.write(str(message.from_user.id) + '__-__' + str(message.text) + ' | ' + strftime("%Y-%m-%d %H:%M:%S",
                                                                                             gmtime()) + '\n')
    print("Done")
    Bot.send_message(message.from_user.id, "Done")

    if_alert = False
