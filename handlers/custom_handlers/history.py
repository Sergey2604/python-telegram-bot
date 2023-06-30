from telebot.types import Message

from database.common.models import db
from loader import bot
from states.user_states import UserInfoState


@bot.message_handler(commands=['history'])
def user_history(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.history, message.chat.id)
    history_create = db.execute_sql("SELECT * FROM history WHERE user_id=? ORDER BY id DESC LIMIT 10",
                                    params=(str(message.from_user.id),))
    for i in history_create:
        bot.send_message(message.from_user.id, ('На дату '+i[1]+' температура в городе '+i[3]+' была '+i[4]))
    bot.set_state(message.from_user.id, UserInfoState.start)
