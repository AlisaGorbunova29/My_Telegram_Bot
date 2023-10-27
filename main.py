from aiogram import Bot, Dispatcher, executor, types
from src.config import token, MainMenu
from src.weather import get_weather
from src.short_info import summary
from src.image import get_picture
from src.attraction import get_attraction
import re

#создание бота
bot = Bot(token)
dp = Dispatcher(bot)

#старт
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Добро пожаловать в телеграм-бот!\nЗдесь Вы можете получить интересующую Вас информацию о любом городе мира.\n', reply_markup=MainMenu)

#кнопки
@dp.callback_query_handler(text = "short info")
async def short_info(message: types.Message):
    await bot.send_message(message.from_user.id, "Введите название города в формате: Инфа - {название города}")

@dp.callback_query_handler(text = "attraction")
async def short_info(message: types.Message):
    await bot.send_message(message.from_user.id, "Введите название города в формате: Достопримечательности - {название города на английском с маленькой буквы!}")

@dp.callback_query_handler(text = "image city")
async def short_info(message: types.Message):
    await bot.send_message(message.from_user.id, "Введите название города в формате: Изображение - {название города}")

@dp.callback_query_handler(text = "weather")
async def weather(message: types.Message):
    await bot.send_message(message.from_user.id, "Введите запрос в формате: Погода - {название города}")

#ответ на запрос
@dp.message_handler()
async def request(message:types.Message):
    try:
        if (re.findall('^Погода - [a-zA-Z]*', message.text)):
            city = message.text[9:]
            answer = get_weather(city)
            await message.reply(answer)
            await bot.send_message(message.from_user.id, 'Хотите узнать что-то ещё?\nМеню:', reply_markup=MainMenu)
        elif (re.findall('^Инфа - [a-zA-Z]*', message.text)):
            city = message.text[7:]
            answer = summary(city)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text = "Хочу больше информации!", url=f"https://ru.wikipedia.org/wiki/{city}"))
            await message.reply(answer, reply_markup=markup)
            await bot.send_message(message.from_user.id, 'Хотите узнать что-то ещё?\nМеню:', reply_markup=MainMenu)
        elif (re.findall('^Достопримечательности - [a-zA-Z]*', message.text)):
            city = message.text[24:]
            answer = get_attraction(city)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text = "Хочу больше информации!", url=f"https://ru.wikipedia.org/wiki/{city}"))
            if (len(answer[0]) > 0):
                photos = answer[1]
                texts = answer[0]
                for i in range(0, len(photos)):
                    await bot.send_message(message.from_user.id, texts[i])
                    photo = types.InputFile.from_url(photos[i])
                    await bot.send_photo(message.from_user.id, photo = photo)
            else:
                await message.reply('К сожалению, найти информацию не удалось')
                photo = types.InputFile.from_url('https://vsememy.ru/kartinki/wp-content/uploads/2023/03/1661951452_1-papik-pro-p-smailik-izvinyayushchiisya-png-1.png')
                await bot.send_photo(message.from_user.id, photo = photo, reply_markup=markup)
            await bot.send_message(message.from_user.id, 'Хотите узнать что-то ещё?\nМеню:', reply_markup=MainMenu)

        elif (re.findall('^Изображение - [a-zA-Z]*', message.text)):
            city = message.text[13:]
            answer = get_picture(city)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text = "Хочу больше изображений!", url=f"https://ru.pinterest.com/search/pins/?q={city}&rs=typed"))
            if (answer):
                photo = types.InputFile.from_url(answer[0])
                await bot.send_photo(message.from_user.id, photo = photo, reply_markup=markup)
            else:
                await bot.send_message(message.from_user.id, 'К сожалению фотографию города получить не удалось')
                photo = types.InputFile.from_url('https://vsememy.ru/kartinki/wp-content/uploads/2023/03/1661951452_1-papik-pro-p-smailik-izvinyayushchiisya-png-1.png')
                await bot.send_photo(message.from_user.id, photo = photo, reply_markup=markup)
            await bot.send_message(message.from_user.id, 'Хотите узнать что-то ещё?\nМеню:', reply_markup=MainMenu)
        else:
            await message.reply('Некорректный ввод')
    except:
        await message.reply('Проверьте название города')
        pass

executor.start_polling(dp)