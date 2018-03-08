import telebot
import bot.constants
import re

Bot = None

start_flag = False


def start(message):
    global Bot
    global start_flag
    Bot.send_message(message.from_user.id, 'Введіть дані \n(Прізвище Ініціали Група)')
    start_flag = True
    print('start')


def check_for_correct(text):
    data = text.split('_')
    flag = False
    if data[0].isalpha() and re.match(r'^[А-Я]', data[0]):
        if data[1].count('.') == 2 and data[1].__len__() == 4 and data[1].endswith('.'):
            if data[2].isdigit():
                flag = True
    return flag


def add_cadet(message):
    global start_flag
    with open('bd.txt', 'a') as fio:
        if check_for_correct(str(message.text)):
            fio.write("hb")
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('Відмітка про перебування поза межами інституту', 'Сповістити про зауваження чи загрозу')
    Bot.send_message(message.from_user.id, '>>>', reply_markup=user_markup)
    start_flag = False
