from pathlib import Path
import sqlite3
from xml.etree.ElementTree import tostring
import TOKEN
from telebot import types
import telebot
# coding: utf-8


bot = telebot.TeleBot(TOKEN.token)  # токен лежит в файле config.py

backtext = 'Назад'
backtextbot = 'Возвращаю в главное меню'
startMessage = 'Вас приветствует виртуальный помощник креативного пространства ИСО800. Здесь вы можете забронировать площадку для фото и видеосъемки, арендовать технику, записаться на мероприятия и многое другое'
mainChatId = "@iso800nn"  # -1001595345813
subscToCh = "Чтобы начать пользоваться ботом, необходимо быть подписанным на канал ИСО800"
notSubText = "Не подписан"
subText = 'Подписан'
btn2txt = ['АРЕНДА ПРОСТРАНСТВА И ОБОРУДОВАНИЯ',
           ['Аренда пространства', ['Белая зона (1200 рублей)', 'Зеленая зона', 'Площадка для мастер-классов', 'Корпоративы']], ['Аренда оборудования', ['Объективы', 'Камеры', 'Постоянный свет', 'Импульсный свет', 'Трансляционное оборудование', 'Стойки, штативы, стабилизация', 'Звуковое оборудование', 'Видеорекордеры']], ]
btn1txt = 'ОБ ИСО'
btn4txt = 'КУРСЫ И МАСТЕР-КЛАССЫ'
btn5txt = ['УСЛУГИ', ['Создание ролика под ключ', 'Работа специалиста по свету (гафер)', 'Работа специалиста по 3д(UnrealEngine)', 'Работа видеографа',
                      'Работа специалиста по цветокоррекции', 'Работа моушн-дизайнера', 'Работа сценариста', 'Работа технического ассистента']]
btn3txt = ['КИНОВЕЧЕРА И РАЗВЛЕЧЕНИЯ', ['Посиделки и киновечера часовой доступ в пространство 200 рублей, в момент киновечера 300 рублей',
                                        'Зона PS5 (300 рублей в час)', 'Зона VR (500 рублей в час)', 'Фотозона (500 рублей 30 мин)']]
btnRename = 'Изменить имя'
reanameTxt = 'Окей. Напиши имя, на которое ты хочешь поменять свое'

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
        for value in sql.execute(f"SELECT * FROM users WHERE id={message.from_user.id}"):
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
    btn2 = types.KeyboardButton(btn2txt[0])
    btn3 = types.KeyboardButton(btn3txt[0])
    btn4 = types.KeyboardButton(btn4txt)
    btn5 = types.KeyboardButton(btn5txt[0])
    btn6 = types.KeyboardButton(btnRename)
    markup.row(btn1)
    markup.row(btn2, btn3)
    markup.row(btn4, btn5)
    markup.row(btn6)
    return markup


def showPuncts(message, btns):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in btns:
        print(i)
        btn = types.KeyboardButton(i)
        markup.add(btn)
    btn3 = types.KeyboardButton(backtext)
    markup.add(btn3)
    bot.send_message(
        message.chat.id, text="Что именно Вам нужно", reply_markup=markup)


def userRename(message):
    sql.execute(
        f"UPDATE users SET name='{message.text}' WHERE id='{message.from_user.id}'")
    db.commit()


def userGetName(message):
    for value in sql.execute(f"SELECT * FROM users WHERE id={message.from_user.id}"):
        return [True, value[2]]


@bot.message_handler(commands=['start'])
def start(message):
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(
        text="Дать свой номер телефона", request_contact=True)
    mark.add(btn1)
    bot.send_message(
        message.chat.id, text="Привет! Мне нужен твой контакт, чтобы понять, знаю ли я тебя", reply_markup=mark)


@bot.message_handler(content_types=['contact'])
def start(message):
    bot.send_message(message.chat.id, text="Смотрю...")
    req = authorization(message=message, phone=message.contact)
    print(req)
    if req[0] == True:
        bot.send_message(message.chat.id, text="Да, вижу тебя")
        bot.send_message(message.chat.id, text=f"Привет, {req[1]}")
    else:
        bot.send_message(
            message.chat.id, text="{req[1]}, не вижу тебя, заношу в бд")
    bot.send_message(message.chat.id, text=startMessage.format(
        message.from_user), reply_markup=mainMenuBack())


@bot.message_handler(content_types=['text'])
def func(message):
    print(message.text)
    print(backtext)
    if(message.text == btn1txt):
        bot.send_message(
            message.chat.id, text="краткая информация о пространстве с фотографиями или видео")
    elif(message.text == backtext):
        bot.send_message(message.chat.id, text=backtextbot,
                         reply_markup=mainMenuBack())
    elif(message.text == btn2txt[0]):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(btn2txt[1][0])
        btn2 = types.KeyboardButton(btn2txt[2][0])
        btn3 = types.KeyboardButton(backtext)
        markup.add(btn1, btn2, btn3)
        bot.send_message(
            message.chat.id, text="Пространство или обурудование?", reply_markup=markup)
    elif(message.text == btn2txt[1][0]):
        showPuncts(message=message, btns=btn2txt[1][1])
    elif(message.text == btn2txt[2][0]):
        showPuncts(message=message, btns=btn2txt[2][1])
    elif(message.text == btn3txt[0]):
        showPuncts(message=message, btns=btn3txt[1])
    elif(message.text == btn4txt):
        bot.send_message(message.chat.id, text="Раздел в разработке")
    elif(message.text == btn5txt[0]):
        showPuncts(message=message, btns=btn5txt[1])
    elif(message.text == btnRename):
        msg = bot.send_message(message.chat.id, text='Окей, ' +
                               userGetName(message=message)[1] + '. Какое имя ты хочешь?')
        bot.register_next_step_handler(msg, userRename)


bot.polling(none_stop=True)
