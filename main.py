from loader import bot
import handlers  # noqa
from utils.set_bot_commands import set_default_commands
from telebot.custom_filters import StateFilter
from work_without_telegram import to_work


if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    to_work()
    bot.infinity_polling()
