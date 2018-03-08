import telebot
import bot.constants
import re

Bot = telebot.TeleBot(bot.constants.token_of_bot)

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
        if re.match(r'^[А-Я].[А-Я].', data[1]):
            if data[2].isdigit():
                flag = True
    return flag


def add_cadet(message):
    global start_flag
    with open('bd.txt', 'a') as fio:
        check_for_correct(str(message.text))
        fio.write(str(message.text) + '\n')
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('Відмітка про перебування поза межами інституту', 'Сповістити про зауваження чи загрозу')
    Bot.send_message(message.from_user.id, '>>>', reply_markup=user_markup)
    start_flag = False
