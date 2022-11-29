import telebot
from telebot import types  # для указание типов
import TOKEN
from xml.etree.ElementTree import tostring
from requests import patch, request
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
CHAT_ID = -1001
subscToCh = "Чтобы начать пользоваться ботом, необходимо быть подписанным на канал ИСО800"


@bot.message_handler(commands=['start'])
def start(message):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton("👋 Поздороваться")
    # btn2 = types.KeyboardButton("❓ Задать вопрос")
    # markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text=startMessage.format(
        message.from_user))
    # reply_markup=markup
    if(chennelCheck() == True):
        bot.send_message(message.chat.id, text="chennelCheck".format(
            message.from_user))
    else:
        bot.send_message(message.chat.id, text=subscToCh.format(
            message.from_user))


def chennelCheck():
    return True


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(
            message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(
            message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif(message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(
            message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(
            message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)
