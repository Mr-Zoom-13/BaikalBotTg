from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import random

TOKEN = '5035911371:AAFzBDVpYqmfmoWTmChBMxwQLLDiZTYKJMw'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
photos_ugadaika = ['baikal-1.jpg', 'baikal-1.jpg', 'baikal-1.jpg', 'baikal-1.jpg',
                   'ilmen-1.jpg', 'ilmen-2.jpg', 'ladoga-1.jpg', 'ladoga-2.jpg', 'chani-1.jpg',
                   'chani-2.jpg']
answers_ugadaika_system = [True, True, True, True, False, False, False, False, False, False]
answers_ugadaika_user_yes = {0: 'Да, это Байкал, верно! Молодец!',
                             4: 'К сожалению нет! Это озеро Ильмень!',
                             5: 'К сожалению нет! Это озеро Ильмень!',
                             6: 'К сожалению нет! Это Ладожское Озеро!',
                             7: 'К сожалению нет! Это Ладожское Озеро!',
                             8: 'К сожалению нет! Это Озеро Чаны!',
                             9: 'К сожалению нет! Это Озеро Чаны!'}
answers_ugadaika_user_no = {0: 'К сожалению нет! Это Озеро Байкал!',
                            4: 'Совершенно верно! Это озеро Ильмень!',
                            5: 'Совершенно верно! Это озеро Ильмень!',
                            6: 'Совершенно верно! Это Ладожское Озеро!',
                            7: 'Совершенно верно! Это Ладожское Озеро!',
                            8: 'Совершенно верно! Это Озеро Чаны!',
                            9: 'Совершенно верно! Это Озеро Чаны!'}
rand_photo = 100
facts = {'Байкал это самое глубокое озеро мира': True,
         'На Байкале обнаружено около ста газовых («грязевых») вулканов': True,
         'В настоящее время на Байкале есть действующие вулканы.': False,
         'Горы вокруг Байкала находятся в постоянном движении: они поднимаются или опускаются.': True,
         'Озеро Байкал переживает около 2000 землетрясений в год.': True,
         'На Байкале происходят настоящие штормы, высота волн которых достигает 100-200 метров!': False,
         'Из Байкала протекает две реки.': False,
         'В месте своего рождения на Байкале река Ангара имеет ширину 1 километр.': True}
random_fact = '0'
keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
button_1 = types.KeyboardButton(text="Викторина")
keyboard.add(button_1)
button_2 = types.KeyboardButton(text="Утверждения")
keyboard.add(button_2)
button_3 = types.KeyboardButton(text="Полезная информация")
keyboard.add(button_3)


@dp.message_handler(commands=['start'])
async def start_func(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="Приветствуем вас в нашем боте, посвященном озеру Байкал! На выбор вам будут предоставлены различные поучительные игры и викторины.",
                           reply_markup=keyboard)


@dp.message_handler(Text(equals="Полезная информация"))
async def usefull_information(message: types.Message):
    await bot.send_message(message.chat.id, "<b>!!! ПОЛЕЗНАЯ ИНФОРМАЦИЯ !!! </b>\n\n<i>Интересные факты: </i>\n 1. faktrus.ru/50-%D1%84%D0%B0%D0%BA%D1%82%D0%BE%D0%B2-%D0%BE-%D0%B1%D0%B0%D0%B9%D0%BA%D0%B0%D0%BB%D0%B5/ \n 2. https://fishki.net/mix/1736633-17-interesnyh-faktov-o-bajkale.html \n\n\n <i>Интересный видеоролик о Байкале - https://yandex.ru/video/preview/?filmId=15400220045413060661&from=tabbar&parent-reqid=1639921319164536-9422180006510794072-vla1-4631-vla-l7-balancer-8080-BAL-649&text=%D0%B1%D0%B0%D0%B9%D0%BA%D0%B0%D0%BB</i> \n\n\n Эта информация может пригодится вам при прохождении наших конкурсов!",
          parse_mode='html', reply_markup=keyboard)


@dp.message_handler(Text(equals="Утверждения"))
async def facts_func(message: types.Message):
    global random_fact
    keyboard2 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text="Да, это верное утверждение!")
    keyboard2.add(button_1)
    button_2 = types.KeyboardButton(text="Нет, это не так!")
    keyboard2.add(button_2)
    random_fact = random.choice(list(facts.keys()))
    await bot.send_message(chat_id=message.chat.id,
                           text=random_fact, reply_markup=keyboard2)


@dp.message_handler(Text(equals="Да, это верное утверждение!"))
async def fact_yes(message: types.Message):
    global random_fact
    if facts[random_fact]:
        await bot.send_message(chat_id=message.chat.id,
                               text="Вы правы! Это верное утверждение!", reply_markup=keyboard)
    else:
        await bot.send_message(chat_id=message.chat.id,
                               text="К сожалению нет! Это неверное утверждение!",
                               reply_markup=keyboard)


@dp.message_handler(Text(equals="Нет, это не так!"))
async def fact_no(message: types.Message):
    global random_fact
    if not facts[random_fact]:
        await bot.send_message(chat_id=message.chat.id,
                               text="Вы правы! Это неверное утверждение!", reply_markup=keyboard)
    else:
        await bot.send_message(chat_id=message.chat.id,
                               text="К сожалению нет! Это верное утверждение!",
                               reply_markup=keyboard)


@dp.message_handler(Text(equals="Викторина"))
async def ugadaika_func(message: types.Message):
    global rand_photo
    rand_photo = random.randint(0, len(photos_ugadaika) - 1)
    photo = InputFile(photos_ugadaika[rand_photo])
    keyboard2 = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text="Да! Это Байкал!")
    keyboard2.add(button_1)
    button_2 = "Нет! Это не Байкал!"
    keyboard2.add(button_2)
    await bot.send_photo(
        caption='Перед вами находится фотография, определите какое это озеро!',
        chat_id=message.chat.id, photo=photo, reply_markup=keyboard2)


@dp.message_handler(Text(equals="Да! Это Байкал!"))
async def ugadaika_yes(message: types.Message):
    global rand_photo
    if answers_ugadaika_system[rand_photo]:
        await message.reply(answers_ugadaika_user_yes[0], reply_markup=keyboard)
    else:
        await message.reply(answers_ugadaika_user_yes[rand_photo], reply_markup=keyboard)


@dp.message_handler(Text(equals="Нет! Это не Байкал!"))
async def ugadaika_no(message: types.Message):
    global rand_photo
    if not answers_ugadaika_system[rand_photo]:
        await message.reply(answers_ugadaika_user_no[rand_photo], reply_markup=keyboard)
    else:
        await message.reply(answers_ugadaika_user_no[0], reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)
