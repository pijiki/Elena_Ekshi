import requests
from datetime import datetime

from datebase import db_history_write, db_history_read


def parser(city):
    try:
        URL = 'https://api.openweathermap.org/data/2.5/weather'
        parametrs = dict(appid='ca5da63a6b720e7a27607013166a1a3a',
                         units='metric', lang='ru')

        parametrs['q'] = city
        data = requests.get(URL, params=parametrs).json()
        temp = data['main']['temp']
        city_name = data['name']
        wind = data['wind']['speed']
        timezone = data['timezone']
        sunrise = data['sys']['sunrise']
        sunrise = datetime.utcfromtimestamp(sunrise + timezone).strftime(
            '%Y-%m-%d %H:%M:%S')
        sunset = data['sys']['sunset']
        sunset = datetime.utcfromtimestamp(sunset + timezone).strftime(
            '%Y-%m-%d %H:%M:%S')
        description = data['weather'][0]['description']
        return (f'В городе {city_name} сейчас {description}'
                f'\nТемпература: {temp}°С'
                f'\nСкорость ветра: {wind} м/с'
                f'\nРассвет: {sunrise}'
                f'\nЗакат: {sunset}')
    except KeyError:
        return 'Вы неправильно ввели город.'
