import re


import unicodedata
import requests
import json
from pprint import pprint
from datetime import datetime
from bs4 import BeautifulSoup


# URL = 'https://api.openweathermap.org/data/2.5/weather'
#
# parametrs = {
#     'appid': 'ca5da63a6b720e7a27607013166a1a3a',
#     'units': 'metric',
#     'lang': 'ru'
# }
# while True:
#     city = input('Введите город для просмотра: ')
#     if not city:
#         break
#     parametrs['q'] = city
#     data = requests.get(URL, params=parametrs).json()
#     temp = data['main']['temp']
#     city_name = data['name']
#     wind = data['wind']['speed']
#     timezone = data['timezone']
#     sunrise = data['sys']['sunrise']
#     sunrise = datetime.utcfromtimestamp(sunrise + timezone).strftime('%Y-%m-%d %H:%M:%S')
#     sunset = data['sys']['sunset']
#     sunset = datetime.utcfromtimestamp(sunset + timezone).strftime('%Y-%m-%d %H:%M:%S')
#     description = data['weather'][0]['description']
#     print(f'''
# В городе \033{city_name}\033[0m сейчас {description}
# Температура: \033[33m{temp}\033[0m°С
# Скорость ветра: \033[35m{wind}\033[0m м/с
# Рассвет: \033[36m{sunrise}\033[0m
# Закат: \033[34m{sunset} \033[0m
#     ''')


## Цитата дня

# api = '13d2b973ed0979c9b1ed70bf5125781b'
# URL = 'https://favqs.com/api/qotd'
#
# pprint(requests.get(URL))
# data = requests.get(URL).json()
# body = data['quote']['body']
#
# print(f'''
# Цитата дня: \033[35m{body}\033[0m
# ''')

## Новости

print('''
1: 'Общество',
2: 'Политика',
3: 'Экономика',
4: 'Спорт',
5: 'Колумнисты',
6: 'Мир'
''')
num_category = int(input('Введите номер категории: '))
URL0 = 'https://www.gazeta.uz/ru/'
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
CATEGORY = ''
html0 = requests.get(URL0, headers=HEADER).text
soup = BeautifulSoup(html0, 'html.parser')

categories = soup.find('ul', class_='nav__container-items')

list_category = []
for category in categories:
    a_category = category.find('a')
    if a_category == -1:
        pass
    else:
        list_category.append(a_category)

for c in list_category:
    a = list_category.index(c)+1
    if a == num_category:
        CATEGORY = str(c).split('/')[2]

URL = URL0 + CATEGORY + '/'
html = requests.get(URL, headers=HEADER).text
articles = soup.find_all('div', class_='nblock')
json_data = []
for article in articles:
    title = article.find('div', class_='nt').find('h3').get_text(strip=True)
    publication = article.find('div', class_='ndt').get_text()
    publication = re.match(r'(\w+, | \d+ \w+ \d+, ) \d\d:\d\d', publication).group()
    description = article.find('div', class_='nt').find('p').get_text()
    image_link = article.find('img').get('data-src')

    json_data.append({
        'title': unicodedata.normalize('NFKD', title),
        'context': unicodedata.normalize('NFKD', description),
        'publication': publication,
        'image_link': image_link
    })

# with open(f'gazeta_{CATEGORY}.json', mode='w', encoding='UTF-8') as file:
#     json.dump(json_data, file, ensure_ascii=False, indent=4)
print(json_data)
