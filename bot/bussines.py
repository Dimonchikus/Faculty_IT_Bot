import telebot
import bot.constants
import re

Bot = None

start_flag = False


def start(message):
    global Bot
    global start_flag
    Bot.send_message(message.from_user.id, 'Введіть дані (українською):\n(Прізвище_Ініціали_Група_Номер телефону)\nЗразок: Шкіцький_В.В._265_+380951234567')
    start_flag = True
    print('start')


def check_for_correct(text):
    data = text.split('_')
    flag = False
    if data[0].isalpha() and re.match(r'^[А-Я,І,і]', data[0]):
        if re.match(r'^[А-Я,І,і].[А-Я,І,і].',data[1]):#data[1].count('.') == 2 and data[1].__len__() == 4 and data[1].endswith('.') and
            if data[2].isdigit() and data[2].__len__() == 3:
                if re.match(r'^\+380[5,6,7,9][0-9]{8}$', data[3]):
                    flag = True
    return flag


def add_cadet(message):
    global start_flag
    with open('bd.txt', 'a', encoding='utf-8') as fio:
        if check_for_correct(str(message.text)):
            fio.write(str(message.from_user.id) + ' ' + str(message.text) + '\n')
            user_markup = telebot.types.ReplyKeyboardMarkup(True)
            user_markup.row('Відмітка про перебування поза межами інституту', 'Сповістити про зауваження чи загрозу')
            Bot.send_message(message.from_user.id, 'Вас успішно занесено до бази даних', reply_markup=user_markup)
            start_flag = False
        else:
             Bot.send_message(message.from_user.id, "Введіть інформацію за поданим зразком")
