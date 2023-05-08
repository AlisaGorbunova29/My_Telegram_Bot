from aiogram import types

#токены
token = "6122502396:AAGWvetQZM8ytpuuBSVkHfA-7AzDxrqY-D8"
weather_token = "2867c707f7ef301bab1411d36ea751e3"

#главное меню
MainMenu = types.InlineKeyboardMarkup()
MainMenu.add(types.InlineKeyboardButton(text = "Погода", callback_data = "weather"))
MainMenu.add(types.InlineKeyboardButton(text = "Достопримечательности городов России", callback_data = "attraction"))
MainMenu.add(types.InlineKeyboardButton(text = "Изображение", callback_data = "image city"))
MainMenu.add(types.InlineKeyboardButton(text = "Краткая информация о городе", callback_data = "short info"))

#эмоджи с погодой
unicode_for_smile_weather = {'Thunderstorm': 'Гроза \U000026c8', 
                             'Drizzle': 'Моросящий дождь \U00002614',
                             'Rain': 'Дождь \U00002614',
                             'Snow': 'Снег \U0001F328',
                             'Clouds': 'Облачно \U00002601',
                             'Atmosphere': 'Туман \U0001F32B',
                             'Clear': 'Солнечно \U00002600'}