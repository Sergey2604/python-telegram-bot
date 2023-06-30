from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):
    city = State()
    form_weather = State()
