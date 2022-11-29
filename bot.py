import telebot
from telebot import types
import TOKEN
from xml.etree.ElementTree import tostring
# from requests import patch, request
import sqlite3
from pathlib import Path
bot = telebot.TeleBot(TOKEN.token)  # токен лежит в файле config.py


# @bot.message_handler(commands=['start'])  # создаем команду
# def start(message):
# markup = types.InlineKeyboardMarkup()
# button1 = types.InlineKeyboardButton(
#     "Сайт Хабр", url='https://habr.com/ru/all/')
# markup.add(button1)
# bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(
#     message.from_user), reply_markup=markup)
startMessage = 'Вас приветствует виртуальный помощник креативного пространства ИСО800. Здесь вы можете забронировать площадку для фото и видеосъемки, арендовать технику, записаться на мероприятия и многое другое'
mainChatId = "@iso800nn"  # -1001595345813
subscToCh = "Чтобы начать пользоваться ботом, необходимо быть подписанным на канал ИСО800"
notSubText = "Не подписан"
subText = 'Подписан'


def check_sub_channel(chat_m):
    print(chat_m['status'])
    if chat_m['status'] != 'left':
        return True
    else:
        return False


@bot.message_handler(commands=['start'])
def start(message):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton("👋 Поздороваться")
    # btn2 = types.KeyboardButton("❓ Задать вопрос")
    # markup.add(btn1, btn2)
    print(message.from_user)
    uid = message.from_user.id
    print(uid)
    print(bot.get_chat_member(chat_id=mainChatId, user_id=uid))
    bot.send_message(message.chat.id, text=startMessage.format(
        message.from_user))
    # if check_sub_channel(bot.get_chat_member(chat_id=mainChatId, user_id=uid)):
    #     bot.send_message(message.chat_id, text=subText)
    # else:
    #     bot.send_message(message.chat_id, text=notSubText)


bot.polling(none_stop=True)
