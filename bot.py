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

db = sqlite3.connect('bd.sqlite', check_same_thread=False)
sql = db.cursor()


def authorization(phone, message):
    print(phone)
    print(message.from_user.id)
    sql.execute("SELECT phone FROM users")
    if sql.fetchone() is None:
        sql.execute("INSERT INTO users VALUES (?, ?, ?)",
                    (message.from_user.id, phone.phone_number, phone.first_name))
        db.commit()
        return [False, phone.first_name]
    else:
        for value in sql.execute("SELECT * FROM users WHERE id='{message.from_user.id}'"):
            return [True, value[2]]


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
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(
        text="Дать свой номер телефона", request_contact=True)
    mark.add(btn1)
    bot.send_message(
        message.chat.id, text="Привет! Мне нужен твой контакт, чтобы понять, знаю ли я тебя", reply_markup=mark)
    # bot.send_message(message.chat.id, text=startMessage.format(
    #     message.from_user), reply_markup=mainMenuBack())


@bot.message_handler(content_types=['contact'])
def start(message):
    bot.send_message(message.chat.id, text="Смотрю...")
    req = authorization(message=message, phone=message.contact)
    if req == True:
        bot.send_message(message.chat.id, text="Да, вижу тебя")
        bot.send_message(message.chat.id, text="Привет, ")
    else:
        bot.send_message(message.chat.id, text="Не вижу тебя, заношу в бд")


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
