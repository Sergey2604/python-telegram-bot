from telebot.types import Message

from database.common.models import db
from loader import bot
from states.user_states import UserInfoState
from work_without_telegram import to_work


# def get_temp_from_database(user:int):
#     get_temp=db.execute_sql("SELECT `message` FROM `history` WHERE `id`=(MAX(`id`)) AND `user_id`=user")
@bot.message_handler(commands=["weather"])
def weather(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.city, message.chat.id)
    bot.send_message(message.chat.id, "Введите город, в котором Вы хотите узнать погоду")


@bot.message_handler(state=UserInfoState.city)
def get_city_and_temp(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.chat.id, 'Сейчас будет исполнено')
        bot.set_state(message.from_user.id, UserInfoState.form_weather, message.chat.id)
        to_work(message.from_user.id, message.text)
        temp = db.execute_sql("SELECT `temp` FROM history WHERE `user_id` = ? AND place=? ORDER BY id DESC LIMIT 1", (
            message.from_user.id, message.text
        ))
        for i in temp:
            bot.send_message(message.chat.id, 'Сейчас в городе {0} {1} градусов'.format(message.text, *i))
    else:
        bot.send_message(message.from_user.id, 'В названии города должны быть только буквы')
