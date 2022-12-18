from pathlib import Path
import sqlite3
from xml.etree.ElementTree import tostring
import TOKEN
from telebot import types
import telebot
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP, WMonthTelegramCalendar
from datetime import datetime
from telebot.types import LabeledPrice, ShippingOption
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


class MyStyleCalendar(DetailedTelegramCalendar):
    # previous and next buttons style. they are emoji now!
    prev_button = "⬅️"
    next_button = "➡️"
    # you do not want empty cells when month and year are being selected
    empty_month_button = ""
    empty_year_button = ""
    max_date = datetime.now()
    min_date = datetime.today().replace(day=1)


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


def userCheck(message):
    sql.execute(f"SELECT id FROM users WHERE id='{message.from_user.id}'")
    if sql.fetchone() is None:
        return False
    else:
        return True


def userRename(message):
    sql.execute(
        f"UPDATE users SET name='{message.text}' WHERE id='{message.from_user.id}'")
    db.commit()


def userGetName(message):
    for value in sql.execute(f"SELECT * FROM users WHERE id={message.from_user.id}"):
        return [True, value[2]]


def startAg(message):
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(
        text="Дать свой номер телефона", request_contact=True)
    mark.add(btn1)
    bot.send_message(
        message.chat.id, text="Привет! Мне нужен твой контакт, чтобы понять, знаю ли я тебя", reply_markup=mark)


@ bot.message_handler(commands=['start'])
def start(message):
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(
        text="Дать свой номер телефона", request_contact=True)
    mark.add(btn1)
    bot.send_message(
        message.chat.id, text="Привет! Мне нужен твой контакт, чтобы понять, знаю ли я тебя", reply_markup=mark)


@ bot.message_handler(content_types=['contact'])
def contact(message):
    userid = message.from_user.id
    # print(userid)  # 852191502
    chatId = -1001595345813
    try:
        result = bot.get_chat_member(chatId, message.from_user.id)
        print(result.status)
        if(result.status == "member" or result.status == "administrator"):
            bot.send_message(message.chat.id, text="Смотрю...")
            req = authorization(message=message, phone=message.contact)
            # print(req)
            if req[0] == True:
                bot.send_message(message.chat.id, text="Да, вижу тебя")
                bot.send_message(message.chat.id, text=f"Привет, {req[1]}")
            else:
                bot.send_message(
                    message.chat.id, text="Не вижу тебя, заношу в бд")
            bot.send_message(message.chat.id, text=startMessage.format(
                message.from_user), reply_markup=mainMenuBack())
        else:
            bot.send_message(
                message.chat.id, text="Ты наверно еще не в нашем канале. Подпишись и заходи ко мне) https://t.me/iso800nn")
    except:
        bot.send_message(
            message.chat.id, text="Ты наверно еще не в нашем канале. Подпишись и заходи ко мне) https://t.me/iso800nn")


@ bot.message_handler(content_types=['text'])
def func(message):
    print(message.text)
    print(backtext)
    if(message.text == btn1txt):
        if(userCheck(message=message) == True):
            bot.send_message(
                message.chat.id, text="краткая информация о пространстве с фотографиями или видео")
        else:
            startAg(message=message)
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
    else:
        sql.execute("SELECT * FROM items")
        if sql.fetchone() is None:
            print('none')
        else:
            for value in sql.execute("SELECT * FROM items"):
                if(message.text == value[1]):
                    x = datetime.now().date()
                    maxim = datetime.now().date().replace(day=1)

                    if(x.day > 1):
                        if(x.month < 12):
                            maxim = datetime.now().date().replace(month=x.month + 1)
                        else:
                            maxim = datetime.now().date().replace(year=x.year + 1)
                    else:
                        print("x <= 1")
                    calendar, step = WMonthTelegramCalendar(
                        max_date=maxim, min_date=x).build()
                    bot.send_message(message.chat.id,
                                     f"Select {LSTEP[step]}",
                                     reply_markup=calendar)


def addDate(message):
    return False


@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(c):
    x = datetime.now().date()
    maxim = datetime.now().date().replace(day=1)
    if(x.day > 1):
        if(x.month < 12):
            maxim = datetime.now().date().replace(month=x.month + 1)
            print(maxim)
        else:
            maxim = datetime.now().date().replace(year=x.year + 1, month=1)
            print(maxim)
    result, key, step = DetailedTelegramCalendar(
        max_date=maxim, min_date=x).process(c.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        print(c.message.chat.id)
        bot.edit_message_text(f"Ваша дата {result}",
                              c.message.chat.id,
                              c.message.message_id)
        bot.send_message(c.message.chat.id, text=c.message.text)


bot.polling(none_stop=True)
