from telebot.types import Message

from loader import bot
from states.user_states import UserInfoState


@bot.message_handler(commands=["weather"])
def weather(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.city, message.chat.id)
    bot.send_message(message.chat.id, "Введите город, в котором Вы хотите узнать погоду")


@bot.message_handler(state=UserInfoState.city)
def get_city(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.chat.id, 'Сейчас будет исполнено')
        bot.set_state(message.from_user.id, UserInfoState.form_weather, message.chat.id)
    else:
        bot.send_message(message.from_user.id, 'В названии города должны быть только буквы')
@bot.message_handler(state=UserInfoState.form_weather)
def form_weather(message:Message)->None:
    bot.send_message(message.chat.id,'Введите одну из команд:\n /current - температура на данный момент, /low - '
                                     'самая низкая температура за определенный промежуток времени, /high - '
                                     'самая высокая температура за определенный промежуток времени')