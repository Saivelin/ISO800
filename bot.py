from pathlib import Path
import sqlite3
from xml.etree.ElementTree import tostring
import TOKEN
from telebot import types
import telebot
from telebot.types import LabeledPrice, ShippingOption
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

prices = []

# for val in sql.execute("SELECT * FROM items"):
# prices.append(LabeledPrice(label=val[1], amount=val[2]))

prices = [LabeledPrice(label='Working Time Machine',
                       amount=5750), LabeledPrice('Gift wrapping', 500)]
shipping_options = [
    ShippingOption(id='instant', title='WorldWide Teleporter').add_price(
        LabeledPrice('Teleporter', 1000)),
    ShippingOption(id='pickup', title='Local pickup').add_price(LabeledPrice('Pickup', 300))]

provider_token = "381764678:TEST:47139"


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
    sql.execute(f"SELECT * FROM users WHERE id={message.from_user.id}")
    if sql.fetchone() is None:
        sql.execute("INSERT INTO users VALUES (?, ?, ?)",
                    (message.from_user.id, phone.phone_number, phone.first_name))
        db.commit()
        return [False, phone.first_name]
    else:
        for value in sql.execute(f"SELECT * FROM users WHERE id={message.from_user.id}"):
            return [True, value[2]]


def check_sub_channel(chat_m):
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
        if(result.status == "member" or result.status == "administrator"):
            bot.send_message(message.chat.id, text="Смотрю...")
            req = authorization(message=message, phone=message.contact)
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
    elif(message.text == "Мои записи"):
        mes = ''
        reses = []
        for res in sql.execute(
                f"SELECT * FROM appointments WHERE userid={message.from_user.id}"):
            reses.append(res)
        for res in reses:
            for val in sql.execute(f"SELECT * FROM items WHERE id={res[1]}"):
                mes += f"\n" + str(val[1]) + " " + \
                    str(val[2]) + ' - ' + str(res[3])
        bot.send_message(message.chat.id, text=mes)
    elif(message.text == btnRename):
        msg = bot.send_message(message.chat.id, text='Окей, ' +
                               userGetName(message=message)[1] + '. Какое имя ты хочешь?')
        bot.register_next_step_handler(msg, userRename)
    elif(message.text == "buy"):
        bot.send_message(message.chat.id,
                         "Real cards won't work with me, no money will be debited from your account."
                         " Use this test card number to pay for your Time Machine: `4242 4242 4242 4242`"
                         "\n\nThis is your demo invoice:", parse_mode='Markdown')
        bot.send_invoice(
            message.chat.id,  # chat_id
            'Working Time Machine',  # title
            ' Want to visit your great-great-great-grandparents? Make a fortune at the races? Shake hands with Hammurabi and take a stroll in the Hanging Gardens? Order our Working Time Machine today!',  # description
            'HAPPY FRIDAYS COUPON',  # invoice_payload
            provider_token,  # provider_token
            'rub',  # currency
            prices,  # prices
            photo_url='http://erkelzaar.tsudao.com/models/perrotta/TIME_MACHINE.jpg',
            photo_height=512,  # !=0/None or picture won't be shown
            photo_width=512,
            photo_size=512,
            is_flexible=False,  # True If you need to set up Shipping Fee
            start_parameter='time-machine-example')
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
                                     f"{message.text}",
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
        else:
            maxim = datetime.now().date().replace(year=x.year + 1, month=1)
    result, key, step = DetailedTelegramCalendar(
        max_date=maxim, min_date=x).process(c.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"Ваша дата {result}",
                              c.message.chat.id,
                              c.message.message_id)
        bot.send_message(c.message.chat.id, text=c.message.text)
        sql.execute(f"SELECT * FROM items WHERE title='{c.message.text}'")
        if sql.fetchone() is None:
            bot.send_message(c.message.chat.id,
                             text="Такого товара не существует")
        else:
            for value in sql.execute(f"SELECT * FROM items WHERE title='{c.message.text}'"):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton(
                    "Снять " + c.message.text + ". На " + str(result))
                btn2 = types.KeyboardButton(backtext)
                markup.add(btn1, btn2)
                msg = bot.send_message(c.message.chat.id,
                                       text=f"Ваш товар: {c.message.text}. Цена: {value[2]}", reply_markup=markup)
                bot.register_next_step_handler(msg, buy)


def buy(message):
    item = message.text.split("Снять")[1].split(".")[0]
    date = message.text.split("На")[1]
    itemid = 0
    item = " ".join(item.split())
    bot.send_message(message.chat.id, text=item)
    print(f"SELECT * FROM items WHERE title='{item}'")
    for res in sql.execute(f"SELECT * FROM items WHERE title='{item}'"):
        itemid = res[0]
        print(res)
    sql.execute(
        f"SELECT * FROM appointments WHERE date='{date}' AND itemid={itemid}")
    if sql.fetchone() is None:
        bot.send_message(message.chat.id, text=message.text + " buy")
        i = pay(message=message, item=item, date=date)
        if(i == True):
            return True
    else:
        bot.send_message(
            message.chat.id, text="Здесь уже занято. Попробуй выбрать другую дату")


def pay(message, item, date):
    # PAYMENT
    success = True
    if(success == True):
        bot.send_message(
            message.chat.id, text="Оплата прошла успешно. Записываю Вас")
        bot.send_message(message.chat.id, text=item)
        item = " ".join(item.split())
        print(f"SELECT * FROM items WHERE title='{item}'")
        for res in sql.execute(f"SELECT * FROM items WHERE title='{item}'"):
            print("sql")
            sql.execute("INSERT INTO appointments(itemid, userid, 'date') VALUES (?, ?, ?)",
                        (res[0], message.from_user.id, date))
            db.commit()
            bot.send_message(message.chat.id, text="Вы записаны")
            return True


@bot.shipping_query_handler(func=lambda query: True)
def shipping(shipping_query):
    print(shipping_query)
    bot.answer_shipping_query(shipping_query.id, ok=True, shipping_options=shipping_options,
                              error_message='Oh, seems like our Dog couriers are having a lunch right now. Try again later!')


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Aliens tried to steal your card's CVV, but we successfully protected your credentials,"
                                                " try to pay again in a few minutes, we need a small rest.")


@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    bot.send_message(message.chat.id,
                     'Hoooooray! Thanks for payment! We will proceed your order for `{} {}` as fast as possible! '
                     'Stay in touch.\n\nUse /buy again to get a Time Machine for your friend!'.format(
                         message.successful_payment.total_amount / 100, message.successful_payment.currency),
                     parse_mode='Markdown')


bot.polling(none_stop=True)
