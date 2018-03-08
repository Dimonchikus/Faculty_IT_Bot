import telebot
import bot.constants

Bot = telebot.TeleBot(bot.constants.token_of_bot)

def start(message):
    global Bot
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('Відмітка про перебування у звільненні(добове)', 'Сповістити про зауваження чи загрозу')
    Bot.send_message(message.from_user.id, 'Введіть дані', reply_markup=user_markup)
    Bot.send_message(message.from_user.id, 'Прізвище')
    Bot.send_message(message.from_user.id, 'Ім\'я')
    Bot.send_message(message.from_user.id, 'Побатькові')
    Bot.send_message(message.from_user.id, 'Звання')
    print('start')



def stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove(True)
    Bot.send_message(message.from_user.id, '...', reply_markup=hide_markup)
    print('Бот зупинено')
