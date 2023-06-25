from telebot.handler_backends import State, StatesGroup


class UserInfoState(StatesGroup):
    city = State()
    city_low = State()
    city_high = State()
    get_date_low = State()
    get_date_high = State()
