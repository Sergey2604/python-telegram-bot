from telebot.types import Message

from loader import bot
from states.user_states import UserInfoState
from work_without_telegram import to_work


# def get_temp_from_database(user:int):
#     get_temp=db.execute_sql("SELECT `message` FROM `history` WHERE `id`=(MAX(`id`)) AND `user_id`=user")
@bot.message_handler(commands=["weather"])
def weather(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.city, message.chat.id)
    bot.send_message(message.chat.id, "Введите город, в котором Вы хотите узнать погоду")


city = None


@bot.message_handler(state=UserInfoState.city)
def get_city(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.chat.id, 'Сейчас будет исполнено')
        bot.set_state(message.from_user.id, UserInfoState.form_weather, message.chat.id)
        to_work(message.from_user.id, message.text)
    else:
        bot.send_message(message.from_user.id, 'В названии города должны быть только буквы')


@bot.message_handler(state=UserInfoState.form_weather)
def form_weather(message: Message) -> None:
    bot.send_message(message.chat.id, 'Сейчас в городе {0} {1} градусов'.format(city, temp))
