from telebot.types import Message

from database.common.models import db
from for_work_files.work_low_and_high import to_work
from loader import bot
from states.user_states import UserInfoState


@bot.message_handler(commands=["low"])
def low(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.city_low, message.chat.id)
    bot.send_message(message.chat.id, "Введите город, в котором Вы хотите узнать минимальную температуру")


@bot.message_handler(state=UserInfoState.city_low)
def get_city(message: Message) -> None:
    if message.text.isalpha() or message.text.__contains__(' '):
        bot.send_message(message.chat.id, 'Введите дату в формате гггг-мм-дд')
        bot.set_state(message.from_user.id, UserInfoState.get_date_low, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['city'] = message.text
    else:
        bot.send_message(message.from_user.id, 'В названии города должны быть только буквы')


@bot.message_handler(state=UserInfoState.get_date_low)
def get_date_and_result_low(message: Message) -> None:
    bot.send_message(message.from_user.id, 'Сейчас будет исполнено')
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        to_work(message.from_user.id, data['city'], message.text, 'low')
        temp = db.execute_sql("SELECT temp FROM history WHERE user_id = ? AND place = ? ORDER BY id DESC LIMIT 1", (
            str(message.from_user.id), str(data['city'])
        ))
    print(temp)
    for i in temp:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            bot.send_message(message.chat.id, 'В городе {0} на дату {1} минимальная температура была {2}'.format(
                data['city'], message.text, *i))
    bot.set_state(message.from_user.id, UserInfoState.start)