import telebot
import bot.constants
import re

Bot = telebot.TeleBot(bot.constants.token_of_bot)

start_flag = False


def start(message):
    global Bot
    global start_flag
    Bot.send_message(message.from_user.id, 'Додайте інформацію про себе (Прізвище_Ініціали_Група)\nЗразок: Шкіцький_В.В._265')
    start_flag = True
    print('start')






def add_cadet(message):
    global start_flag
    with open('bd.txt', 'a') as fio:
        fio.write(str(message.text) + '\n')
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('Відмітка про перебування у звільненні(добове)', 'Сповістити про зауваження чи загрозу')
    Bot.send_message(message.from_user.id, '>>>', reply_markup=user_markup)
    start_flag = False
