import telebot
from telebot import types
import TOKEN
from xml.etree.ElementTree import tostring
import sqlite3
from pathlib import Path

bot = telebot.TeleBot(TOKEN.token)  # токен лежит в файле config.py

startMessage = 'Вас приветствует виртуальный помощник креативного пространства ИСО800. Здесь вы можете забронировать площадку для фото и видеосъемки, арендовать технику, записаться на мероприятия и многое другое'
mainChatId = "@iso800nn"  # -1001595345813
subscToCh = "Чтобы начать пользоваться ботом, необходимо быть подписанным на канал ИСО800"
notSubText = "Не подписан"
subText = 'Подписан'
btn1txt = 'ОБ ИСО'
btn2txt = 'АРЕНДА ПРОСТРАНСТВА И ОБОРУДОВАНИЯ'
btn3txt = 'КИНОВЕЧЕРА И РАЗВЛЕЧЕНИЯ'
btn4txt = 'КУРСЫ И МАСТЕР-КЛАССЫ'
btn5txt = 'УСЛУГИ'
btn2txttxt1 = "Аренда пространства"
btn2txttxtsec = "Аренда оборудования"

db = sqlite3.connect('bd.sqlite')
sql = db.cursor()


def check_sub_channel(chat_m):
    print(chat_m['status'])
    if chat_m['status'] != 'left':
        return True
    else:
        return False


def mainMenuBack():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(btn1txt)
    btn2 = types.KeyboardButton(btn2txt)
    btn3 = types.KeyboardButton(btn3txt)
    btn4 = types.KeyboardButton(btn4txt)
    btn5 = types.KeyboardButton(btn5txt)
    markup.row(btn1)
    markup.row(btn2, btn3)
    markup.row(btn4, btn5)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text=startMessage.format(
        message.from_user), reply_markup=mainMenuBack())


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == btn1txt):
        bot.send_message(
            message.chat.id, text="краткая информация о пространстве с фотографиями или видео")
    elif(message.text == btn2txt):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(btn2txttxt1)
        btn2 = types.KeyboardButton(btn2txttxtsec)
        markup.add(btn1, btn2)
        bot.send_message(
            message.chat.id, text="краткая информация о пространстве с фотографиями или видео", reply_markup=markup)
    elif(message.text == btn2txttxt1):
        bot.send_message(message.chat.id, text=btn2txttxt1)
    elif(message.text == btn2txttxtsec):
        bot.send_message(message.chat.id, text=btn2txttxtsec)


bot.polling(none_stop=True)
