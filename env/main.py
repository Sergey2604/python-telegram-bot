import telebot

import tokens

bot_api = tokens.telegram_bot_api

bot = telebot.TeleBot(bot_api)


@bot.message_handler(['start', 'begin', 'Привет', 'привет', 'hello-world'])
def message_hi(mess):
    bot.reply_to(mess,
                 'Здравствуйте! Я бот по поиску отелей! Напишите, пожалуйста, город, в котором Вы хотите найти отель.')




@bot.message_handler(['help','помощь'])
def message_help(mess):
    bot.reply_to(mess,
                 'Вы можете воспользоваться следующими командами для работы с ботом:\n'
                 '/help - помощь по командам;\n/low - поиск и сортировка отелей от минимальной цены к максимальной\n'
                 '/high - поиск и сортировка отелей от максимальной цены до минимальной\n'
                 '/custom - расширенный поиск отелей\n/history - последние 10 запросов'
                 )


@bot.message_handler(func=lambda message_hi: True)
def echo_message(mess):
    bot.reply_to(mess, mess.text)
@bot.message_handler(func=lambda message_help: True)
def echo_message(mess):
    bot.reply_to(mess, mess.text)


bot.infinity_polling()
