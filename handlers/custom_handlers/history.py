from telebot.types import Message

from database.common.models import db
from loader import bot
from states.user_states import UserInfoState


@bot.message_handler(commands=['history'])
def user_history(message:Message)->None:
    bot.set_state(message.from_user.id, UserInfoState.history, message.chat.id)
    history_create=db.execute_sql("SELECT created_at FROM history WHERE user_id=? ORDER BY id DESC LIMIT 10",params=(str(message.from_user.id),))
    history_city=db.execute_sql("SELECT place FROM history WHERE user_id=? ORDER BY id DESC LIMIT 10",params=(str(message.from_user.id),))
    history_temp=db.execute_sql("SELECT temp FROM history WHERE user_id=? ORDER BY id DESC LIMIT 10",params=(str(message.from_user.id),))
    for i in history_create:
        for j in history_city:
            for k in history_temp:
                answer=*i,*j,*k
                print(answer)
                bot.send_message(message.chat.id,text=answer)