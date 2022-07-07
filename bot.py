import telebot
import pickle
from telebot import types  # для указание типов
import json

settings = {}

with open('bot_settings.json', encoding='utf-8') as json_file:
    settings = json.load(json_file)

model_filename = settings["model_path"]
tfidf_filename = settings["vectorizer_path"]

# загрузка файлов с векторизацией и моделью машинного 
model = pickle.load(open(model_filename, 'rb'))
tfidf = pickle.load(open(tfidf_filename, 'rb'))

bot = telebot.TeleBot(settings["token"])

def calc_feedback2(message):
    chat_id = message.chat.id
    vectorized = tfidf.transform([message.text])
    result = model.predict(vectorized)[0]
    if result == 0:
        bot.send_message(chat_id, text='Возвращайтесь снова! Мы учтем ваши пожелания.')
    elif result == 1:
        bot.send_message(chat_id, text='Рады, что Вам понравилось!')
    elif result == 2:
        bot.send_message(chat_id, text='Жаль, что Вы остались недовольны. Мы учтем ваши пожелания.')

def calc_feedback(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, text='Напишите ваш отзыв:')
    bot.register_next_step_handler(message, calc_feedback2)
    

def car_station(chat_id):
    bot.send_message(chat_id, text='Вы можете поехать на автобусе № 17, 22, 2, 3, 86, 52 или маршрутном такси № 104, 180, 19, 25, 30, 4, 41, 43, 6, 7, 83, 87, 92, 94, 95, 98 до Платановой аллеи/магазина Мелодия, далее пешком (4 минуты).')


def train_station(chat_id):
    bot.send_message(chat_id, text='Вы можете поехать автобусом № 17, 2, 3, 86, либо маршрутным такси № 104, 180, 19, 25, 30, 4, 41, 43, 6, 7, 83, 87, 92, 94, 95, 98 до остановки "Платановая аллея/Магазин Мелодия", затем пройти пешком 370 метров.')


def airoport(chat_id):
    bot.send_message(chat_id, text='Вы можете поехать электричкой до ж/д вокзала Сочи, далее автобусом № 17, 2, 3, 86, либо маршрутным такси № 104, 180, 19, 25, 30, 4, 41, 43, 6, 7, 83, 87, 92, 94, 95, 98 до остановки "Платановая аллея/Магазин Мелодия", затем пройти пешком 370 метров.')


def print_location(chat_id):
    bot.send_message(chat_id, text='Сочи, ул. Несебрская, д. 6')


def print_description(chat_id):
    bot.send_message(chat_id, text='''Marina Yacht Hotel Sochi» ждёт всех гостей солнечного Сочи. К Вашим услугам Wi-Fi, парковка (по предварительному запросу), экскурсионное обслуживание, прокат авто, яхт/катеров, прачечная и другое.
Каждый из номеров подарит Вам максимум положительных эмоций от проживания. Дизайн интерьеров продуман до мельчайших подробностей. Приятные оттенки располагают к прекрасному отдыху после трудового дня.
Отель находится в самом сердце города. В паре шагов морской порт, пляжи, рестораны, магазины, зелёные парки, словом, вся необходимая инфраструктура. До ж/д вокзала всего 10 минут езды.''')

    def print_description(chat_id):
        pass

    def print_description(chat_id):
        pass

    def print_description(chat_id):
        pass

    def print_description(chat_id):
        pass

    def print_description(chat_id):
        pass

    def print_description(chat_id):
        pass


def print_review(chat_id):
    bot.send_message(chat_id, text='''ВЕЛИКОЛЕПНО Остался доволен работой персонала — очень вежливый приветливый администратор, заселение прошло быстро, без каких-либо проблем. Номер достался чистый, просторный, уборка проводилась каждый день. Отдельно хочу отметить расположение отеля — буквально на пристани, в двух шагах от моря. Понравился завтрак, всегда кормили вкусно, меню было разнообразным, а блюда красиво оформленными. Минусов за время проживания не обнаружил.''')


def print_transit(chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('От автовокзала')
    itembtn2 = types.KeyboardButton('От ж/д вокзала')
    itembtn3 = types.KeyboardButton('От аэропорта')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(chat_id, "Выберите опцию:", reply_markup=markup)
    pass


def print_service(chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Сервисы')
    itembtn2 = types.KeyboardButton('Спорт и Отдых')
    itembtn3 = types.KeyboardButton('Питание и напитки')
    itembtn4 = types.KeyboardButton('Детям')
    itembtn5 = types.KeyboardButton('Интернет')
    itembtn6 = types.KeyboardButton('Прокат')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.send_message(chat_id, "Выберите опцию:", reply_markup=markup)


def calc_price(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('1')
    itembtn2 = types.KeyboardButton('2')
    markup.add(itembtn1, itembtn2)
    bot.send_message(
        message.chat.id, text="Укажите количество человек", reply_markup=markup)
    # первый аргумент: message - объект сообщения
    # второй аргумент: функция, которая будет выполняться далее
    # далее можно аргументы передавать в любом количестве через запятую, а принимающая функция должна иметь столько же аргументов, сколько было передано
    bot.register_next_step_handler(message, calc_price_days)

def calc_price_days(message):
    persons = str(message.text)
    if(persons.isdigit()):
        persons = int(persons)
        if(persons in range(1, 3)):
            bot.send_message(message.chat.id, text="Укажите количество ночей")
            bot.register_next_step_handler(message, calc_full_price, persons)
        else:
            bot.send_message(
                message.chat.id, text="К сожалению, у нас нет таких номеров")
            bot.register_next_step_handler(message, calc_price_days)
    else:
        bot.send_message(message.chat.id, text="Укажите число")
        bot.register_next_step_handler(message, calc_price_days)


def calc_full_price(message, persons):
    days = str(message.text)
    if(days.isdigit()):
        days = int(days)
        price = 0
        if(persons == 1):
            price = 3600
        elif(persons == 2):
            price = 3900
        fullprice = days * price
        bot.send_message(message.chat.id, text=f'Цена {fullprice}')
    else:
        bot.send_message(message.chat.id, text="Укажите число")
        bot.register_next_step_handler(message, calc_full_price, persons)


@ bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Расположение')
    itembtn2 = types.KeyboardButton('Описание')
    itembtn3 = types.KeyboardButton('Отзывы')
    itembtn4 = types.KeyboardButton('Проезд')
    itembtn5 = types.KeyboardButton('Услуги')
    itembtn6 = types.KeyboardButton('Забронировать')
    itembtn7 = types.KeyboardButton('Оставить отзыв')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7)
    bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)


@ bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Расположение"):
        print_location(message.chat.id)
    elif (message.text == 'Описание'):
        print_description(message.chat.id)
    elif(message.text == 'Отзывы'):
        print_review(message.chat.id)
    elif(message.text == 'Проезд'):
        print_transit(message.chat.id)
    elif(message.text == 'Услуги'):
        print_service(message.chat.id)
    elif(message.text == 'От автовокзала'):
        car_station(message.chat.id)
    elif(message.text == 'От ж/д вокзала'):
        train_station(message.chat.id)
    elif(message.text == 'От аэропорта'):
        car_station(message.chat.id)
    elif(message.text == 'Забронировать'):
        calc_price(message)
    elif(message.text == 'Оставить отзыв'):
        calc_feedback(message)


bot.polling(none_stop=True)
