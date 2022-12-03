import telebot
from telebot import types
bot= telebot.TeleBot('5966133601:AAF3RICaY1p8ShnBO_RlmA80ExtgM1SkXq0')


@bot.message_handler(commands=['start'])
def start(message):
    mess=f'Вас приветствует виртуальный помощник креативного пространства ИСО800. Здесь вы можете забронировать площадку для фото и видеосъемки, арендовать технику, записаться на мероприятия и многое другое.'
    bot.send_message(message.chat.id, mess, parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id,f'Ваш Никнейм: <b>{message.from_user.username} </b>', parse_mode='html')
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    YES=types.KeyboardButton('Да')
    NO=types.KeyboardButton('Нет')
    markup1.add(YES, NO)
    bot.send_message(message.chat.id,f'Оставляем?', reply_markup=markup1)

@bot.message_handler(commands=['ВЫЙТИ'])
def OBISO(message):
    bot.send_message(message.chat.id, 'До новых встреч', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    tyr=types.KeyboardButton('/start')
    markup3.add(tyr)
    bot.send_message(message.chat.id,f'.', reply_markup=markup3)   
#---------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['ОБ_ИСО800'])
def OBISO(message):
    bot.send_message(message.chat.id, 'ОБ_ИСО800', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    tyr=types.KeyboardButton('Назад')
    markup3.add(tyr)
    bot.send_message(message.chat.id,f'КАКАЯ-ТО ИНФОРМАЦИЯ ПРО ИСО800', reply_markup=markup3)
#---------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['АРЕНДА_ПРОСТРАНСТВА_И_ОБОРУДОВАНИЯ'])
def OBISO(message):
    bot.send_message(message.chat.id, 'АРЕНДА_ПРОСТРАНСТВА_И_ОБОРУДОВАНИЯ', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    AR=types.KeyboardButton('/Aренда_пространства')
    AO=types.KeyboardButton('/Aренда_оборудования')
    tyr=types.KeyboardButton('Назад')
    markup.add(AR,AO,tyr)
    bot.send_message(message.chat.id,f'.', reply_markup=markup)

@bot.message_handler(commands=['Вернуться_к_арендам'])
def OBISO(message):
    bot.send_message(message.chat.id, 'АРЕНДА_ПРОСТРАНСТВА_И_ОБОРУДОВАНИЯ', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    AR=types.KeyboardButton('/Aренда_пространства')
    AO=types.KeyboardButton('/Aренда_оборудования')
    tyr=types.KeyboardButton('Назад')
    markup.add(AR,AO,tyr)
    bot.send_message(message.chat.id,f'.', reply_markup=markup)

@bot.message_handler(commands=['Aренда_пространства'])
def OBISO(message):
    bot.send_message(message.chat.id, 'Aренда пространства', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    AR=types.KeyboardButton('Белая зона (1200 рублей)')
    AO=types.KeyboardButton('Зеленая зона')
    AE=types.KeyboardButton('Площадка для мастер-классов')
    AT=types.KeyboardButton('Kорпоративы')
    tyr=types.KeyboardButton('/Вернуться_к_арендам')
    EX=types.KeyboardButton('Назад')
    markup.add(AR,AO,AE,AT,tyr,EX)
    bot.send_message(message.chat.id,f'👇', reply_markup=markup)

@bot.message_handler(commands=['Aренда_оборудования'])
def OBISO(message):
    bot.send_message(message.chat.id, 'Aренда оборудования', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    AR=types.KeyboardButton('/С_собой')
    AO=types.KeyboardButton('/В_студии')
    tyr=types.KeyboardButton('/Вернуться_к_арендам')
    EX=types.KeyboardButton('Назад')
    markup.add(AR,AO,tyr,EX)
    bot.send_message(message.chat.id,f'.', reply_markup=markup)

@bot.message_handler(commands=['Вернуться_назад'])
def OBISO(message):
    bot.send_message(message.chat.id, 'Aренда оборудования', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    AR=types.KeyboardButton('/С_собой')
    AO=types.KeyboardButton('/В_студии')
    EX=types.KeyboardButton('Назад')
    markup.add(AR,AO,EX)
    bot.send_message(message.chat.id,f'.', reply_markup=markup)

@bot.message_handler(commands=['С_собой'])
def OBISO(message):
    bot.send_message(message.chat.id, 'Aренда оборудования', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    A1=types.KeyboardButton('Объективы')
    A2=types.KeyboardButton('Камеры')
    A3=types.KeyboardButton('Постоянный свет')
    A4=types.KeyboardButton('Импульсный свет')
    A5=types.KeyboardButton('Трансляционное оборудование')
    A6=types.KeyboardButton('Стойки, штативы, стабилизация')
    A7=types.KeyboardButton('Звуковое оборудование')
    A8=types.KeyboardButton('Видеорекордеры')
    tyr=types.KeyboardButton('/Вернуться_назад')
    EX=types.KeyboardButton('Назад')
    markup.add(A1,A2,A3,A4,A5,A6,A7,A8,EX,tyr)
    bot.send_message(message.chat.id,f'.', reply_markup=markup)

@bot.message_handler(commands=['В_студии'])
def OBISO(message):
    bot.send_message(message.chat.id, 'Aренда оборудования', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    A1=types.KeyboardButton('Объективы')
    A2=types.KeyboardButton('Камеры')
    A3=types.KeyboardButton('Постоянный свет')
    A4=types.KeyboardButton('Импульсный свет')
    A5=types.KeyboardButton('Трансляционное оборудование')
    A6=types.KeyboardButton('Стойки, штативы, стабилизация')
    A7=types.KeyboardButton('Звуковое оборудование')
    A8=types.KeyboardButton('Видеорекордеры')
    tyr=types.KeyboardButton('/Вернуться_назад')
    EX=types.KeyboardButton('Назад')
    markup.add(A1,A2,A3,A4,A5,A6,A7,A8,EX,tyr)
    bot.send_message(message.chat.id,f'.', reply_markup=markup)
#---------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['КИНОВЕЧЕРА_И_РАЗВЛЕЧЕНИЯ'])
def OBISO(message):
    bot.send_message(message.chat.id, 'КИНОВЕЧЕРА_И_РАЗВЛЕЧЕНИЯ', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    A1=types.KeyboardButton('Посиделки и киновечера часовой доступ в пространство 200 рублей, в момент киновечера 300 рублей')
    A2=types.KeyboardButton('Зона PS5 (300 рублей в час)')
    A3=types.KeyboardButton('Зона VR (500 рублей в час)')
    A4=types.KeyboardButton('Фотозона (500 рублей 30 мин)')
    tyr=types.KeyboardButton('Назад')
    markup.add(A1,A2,A3,A4,tyr)
    bot.send_message(message.chat.id,f'.', reply_markup=markup)

#---------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['КУРСЫ_И_МАСТЕР-КЛАССЫ'])
def OBISO(message):
    bot.send_message(message.chat.id, 'КУРСЫ_И_МАСТЕР-КЛАССЫ', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    tyr=types.KeyboardButton('Назад')
    markup.add(tyr)
    bot.send_message(message.chat.id,f'.', reply_markup=markup)
#---------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['УСЛУГИ'])
def OBISO(message):
    bot.send_message(message.chat.id, 'КИНОВЕЧЕРА_И_РАЗВЛЕЧЕНИЯ', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    A1=types.KeyboardButton('Создание ролика под ключ')
    A2=types.KeyboardButton('Работа специалиста по свету (гафер)')
    A3=types.KeyboardButton('Работа специалиста по 3д(UnrealEngine)')
    A4=types.KeyboardButton('Работа видеографа')
    A5=types.KeyboardButton('Работа специалиста по цветокоррекции')
    A6=types.KeyboardButton('Работа моушн-дизайнера')
    A7=types.KeyboardButton('Работа сценариста')
    A8=types.KeyboardButton('Работа технического ассистента')
    tyr=types.KeyboardButton('Назад')
    markup.add(A1,A2,A3,A4,A5,A6,A7,A8,tyr)
    bot.send_message(message.chat.id,f'.', reply_markup=markup)


#---------------------------------------------------------------------------------------------------------------------------------


@bot.message_handler()
def user(message):
    if message.text.lower() == "Нет":
        bot.send_message(message.chat.id,f'Изменить можно тут(Но не факт что правильно): https://t.me/{message.from_user.username}', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        tyr=types.KeyboardButton('Да')
        markup.add(tyr)
        bot.send_message(message.chat.id,f'По готовности нажмите <да>', reply_markup=markup)
    if message.text.lower() == "да":
        bot.send_message(message.chat.id,f'Привет, <b>{message.from_user.username} </b>!', parse_mode='html',reply_markup=types.ReplyKeyboardRemove())
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        ISO=types.KeyboardButton('/ОБ_ИСО800')
        ARD=types.KeyboardButton('/АРЕНДА_ПРОСТРАНСТВА_И_ОБОРУДОВАНИЯ')
        KR=types.KeyboardButton('/КИНОВЕЧЕРА_И_РАЗВЛЕЧЕНИЯ')
        KMK=types.KeyboardButton('/КУРСЫ_И_МАСТЕР-КЛАССЫ')
        U=types.KeyboardButton('/УСЛУГИ')
        R=types.KeyboardButton('/ВЫЙТИ')
        markup2.add(ISO,ARD,KR,KMK,U,R)
        bot.send_message(message.chat.id,'ВЫБЕРИТЕ ДЕЙСТВИЕ', reply_markup=markup2)
    if message.text.lower() == "назад":
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        IS=types.KeyboardButton('/ОБ_ИСО800')
        AR=types.KeyboardButton('/АРЕНДА_ПРОСТРАНСТВА_И_ОБОРУДОВАНИЯ')
        K=types.KeyboardButton('/КИНОВЕЧЕРА_И_РАЗВЛЕЧЕНИЯ')
        KM=types.KeyboardButton('/КУРСЫ_И_МАСТЕР-КЛАССЫ')
        Ui=types.KeyboardButton('/УСЛУГИ')
        R=types.KeyboardButton('/ВЫЙТИ')
        mark.add(IS,AR,K,KM,Ui,R)
        bot.send_message(message.chat.id,'ВЫБЕРИТЕ ДЕЙСТВИЕ', reply_markup=mark)


bot.polling(none_stop=True)