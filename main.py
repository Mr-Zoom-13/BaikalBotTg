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


@dp.message_handler(commands=['start'])
async def start_func(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text="Викторина!")
    keyboard.add(button_1)
    await bot.send_message(chat_id=message.chat.id,
                           text="Приветствуем вас в нашем боте, посвященном озеру Байкал! На выбор вам будут предоставлены различные поучительные игры и викторины.",
                           reply_markup=keyboard)


@dp.message_handler(Text(equals="Викторина!"))
async def ugadaika_func(message: types.Message):
    global rand_photo
    rand_photo = random.randint(0, len(photos_ugadaika) - 1)
    photo = InputFile(photos_ugadaika[rand_photo])
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text="Да! Это Байкал!")
    keyboard.add(button_1)
    button_2 = "Нет! Это не Байкал!"
    keyboard.add(button_2)
    await bot.send_photo(
        caption='Перед вами находится фотография, определите какое это озеро!',
        chat_id=message.chat.id, photo=photo, reply_markup=keyboard)


@dp.message_handler(Text(equals="Да! Это Байкал!"))
async def answer_yes(message: types.Message):
    global rand_photo
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text="Викторина!")
    keyboard.add(button_1)
    if answers_ugadaika_system[rand_photo]:
        await message.reply(answers_ugadaika_user_yes[0], reply_markup=keyboard)
    else:
        await message.reply(answers_ugadaika_user_yes[rand_photo], reply_markup=keyboard)


@dp.message_handler(Text(equals="Нет! Это не Байкал!"))
async def answer_no(message: types.Message):
    global rand_photo
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    button_1 = types.KeyboardButton(text="Викторина!")
    keyboard.add(button_1)
    if not answers_ugadaika_system[rand_photo]:
        await message.reply(answers_ugadaika_user_no[rand_photo], reply_markup=keyboard)
    else:
        await message.reply(answers_ugadaika_user_no[0], reply_markup=keyboard)


if __name__ == '__main__':
    executor.start_polling(dp)
