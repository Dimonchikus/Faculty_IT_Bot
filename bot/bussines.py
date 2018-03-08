import telebot
import bot.constants

Bot = telebot.TeleBot(bot.constants.token_of_bot)

def start(message):
    global Bot
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('Відмітка про перебування у звільненні(добове)', 'Сповістити про зауваження чи загрозу')
    Bot.send_message(message.from_user.id, '>>>', reply_markup=user_markup)
    print('start')



def stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove(True)
    Bot.send_message(message.from_user.id, '...', reply_markup=hide_markup)
    print('Бот зупинено')
