import requests
from src.config import unicode_for_smile_weather, weather_token

#парсит сайт с погодой и достаёт информацию про погоду в городе
def get_weather(city):
    request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric')
    info = request.json()
    temperature = info['main']['temp']
    feels_like = info['main']['feels_like']
    pressure = info['main']['pressure']
    weather = unicode_for_smile_weather[info['weather'][0]['main']]
    return f'В городе {city}:\nТемпература {temperature} \U00002103\nОщущается как {feels_like} \U00002103\nДавление {pressure} Па\n{weather}'


