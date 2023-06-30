import main
if __name__=='__main__':
    bot=main.bot

    @bot.message_handler(['start', 'begin', 'Привет', 'привет', 'hello-world'])
    def message(mess):
        bot.reply_to(mess,
                     'Вы можете воспользоваться следующими командами для работы с ботом:\n'
                     '/help - помощь по командам;\n/low - поиск и сортировка отелей от минимальной цены к максимальной\n'
                     '/high - поиск и сортировка отелей от максимальной цены до минимальной\n'
                     '/custom - расширенный поиск отелей\n/history - последние 10 запросов'
                     )

    @bot.message_handler(func=lambda message: True)
    def echo_message(mess):
        bot.reply_to(mess, mess.text)
