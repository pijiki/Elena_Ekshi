from pprint import pprint

"""
1) Есть два словаря, объедините их:
"""

dict1 = {
    'meat': 90,
    'milk': 15,
    'bread': 3,
    'potato': 6,
    'apple': 20,
    'banana': 25,
    'chicken wings': 45,
    'chocolate': 17
}

dict2 = {
    'kiwi': 30,
    'orange': 25,
    'coca-cola': 10,
    'chips': 18
}

dict1.update(dict2)

pprint(dict1)


"""
2) Напишите сценарий Python для создания и печати словаря, содержащего число 
(от 1 до n включительно) (где n — введенное пользователем число) в форме 
(x, x * x).
"""

n = int(input('Введите число: '))

dict1 = {i: i * i for i in range(1, n + 1)}
print(dict1)


"""
3) Напишите код для суммирования всех значений словаря и вывод среднего 
арифметического значения.
"""

n = int(input('Введите число: '))
dict1 = {i: i * i for i in range(1, n + 1)}
sum_v = sum(dict1.values())
print(f'Сумма всех значений: {sum_v}')
print(f'Среднее арифметическое: {sum_v / n}')


"""
4) Напишите код для объединения двух списков в словарь ключ: значение. СПИСКИ 
ДОЛЖНЫ БЫТЬ ОДНОГО РАЗМЕРА (содержимое списков произвольный)
"""

list_1 = ['6', '7', '8', '9', '10']
list_2 = ['one', 'two', 'three', 'four', 'five']

# 1 способ:

dict1 = {i[0:]: 0 for i in list_1}
dict1['6'] = 'one'
dict1['7'] = 'two'
dict1['8'] = 'three'
dict1['9'] = 'four'
dict1['10'] = 'five'

print(dict1)

# 2 способ:

dict2 = {i: y for i, y in zip(list_1, list_2)}
print(dict2)


"""
5) Есть словарь координат городов. Составьте словарь расстояний между городами
по формуле.
"""

cities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

moscow = cities['Moscow']
london = cities['London']
paris = cities['Paris']

x1 = moscow[0]
x2 = london[0]
x3 = paris[0]

y1 = moscow[1]
y2 = london[1]
y3 = paris[1]


distances = {
    'London-Paris': round(((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5, 4),
    'Moscow-London': round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 4),
    'Moscow-Paris': round(((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5, 4)
}

print(distances)


"""
1) Есть кортеж 
Выведите в отдельный кортеж числа, которые меньше или равны 5 и числа, которые
больше 5.
"""

a = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)

tuple1 = [i for i in a if i <= 5]
tuple2 = [i for i in a if i > 5]

print(f'Кортеж чисел меньше или равных 5: {tuple(tuple1)}')
print(f'Кортеж чисел больше 5: {tuple(tuple2)}')


"""
2) Вы принимаете от пользователя его имя, фамилию, возраст. Сохраните их в 
соответствующие переменные. Сохраните полученные значения в кортеж.
"""

name = input('Введите ваше имя: ')
family_name = input('Введите вашу фамилию: ')
age = input('Введите ваш возраст: ')
list1 = [name, family_name, age]

print(f'Кортеж данных пользователя: {tuple(list1)}')


"""
3) Напишите программу, которая принимает от пользователя секвенцию чисел, 
разделенных запятой и пробелом. После чего запишите каждое число в кортеж.
"""

str1 = input('Введите секвенцию чисел разделенных запятой и пробелом: ')
list1 = str.split(', ')
print(f'Кортеж чисел: {tuple(list1)}')


"""
4)  Напишите программу, которая будет принимать три имени в качестве входных 
данных от пользователя в одном input() и превращать данные в кортеж, ну а 
затем доставать их.
"""

str1 = input('Введите три любых имени разделенные между собой пробелом: ')
list1 = str1.split(' ')
print(f'Кортеж имен: {tuple(list1)}')
print(f'Первое имя: {list1[0]}')
print(f'Второе имя: {list1[1]}')
print(f'Третье имя: {list1[2]}')


"""
5) Дан кортеж чисел numbers = (1, 2, 3, 4, 5, 6, 7). напишите программу, 
которая превращает каждый элемент кортежа в его квадрат и образует второй 
кортеж.
"""

numbers = (1, 2, 3, 4, 5, 6, 7)
print(f'Кортеж чисел: {numbers}')
list_numbers = [i*i for i in numbers]
print(f'Кортеж квадратов: {tuple(list_numbers)}')


"""
6) Напишите программу, которая выводит все четные числа из кортежа в исходном 
порядке, и останавливается когда число равно 815.
"""

numbers = (386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
           953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866,
           950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767,
           553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527)

ind815 = numbers.index(815)
list_numbers = [i for i in numbers[:ind815] if i % 2 == 0]

print(tuple(list_numbers))


"""
7) Есть кортеж с данными, создайте список и кортеж данных без дубликатов.
"""

numbers = (12, 33, 44, 33, 12, 45, 11, 55, '44', 30, 10)
numbers = set(numbers)
print(list(numbers))
print(tuple(numbers))


"""
8) Получите кортеж VLANов со строки:
- общих vlan
- vlan которые есть в config_sw1 но нет в config_sw2
- уникальные vlan c двух сторон
- все vlan без дубликатов
"""

config_sw1 = 'switchport trunk allowed vlan 10,20,30,40,50,70'
config_sw2 = 'switchport trunk allowed vlan 80,90,10,45,50,100'

config_sw1 = config_sw1.split()[4]
config_sw2 = config_sw2.split()[4]

set_config_sw1 = set(config_sw1.split(','))
set_config_sw2 = set(config_sw2.split(','))

print(tuple(set_config_sw1.intersection(set_config_sw2)))
print(tuple(set_config_sw1.difference(set_config_sw2)))
print(tuple(set_config_sw1.symmetric_difference(set_config_sw2)))
print(tuple(set_config_sw1.union(set_config_sw2)))


"""
1) В задании создан словарь, с информацией о разных устройствах.

Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1). 
И вывести информацию о соответствующем устройстве
"""

devices = {
    'r1': {
        'location': 'Bukhara',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': 'Samarkand',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': 'Tashkent',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

dev = input('Введите название устройства [r1/r2/sw1]: ')

for device in devices:
    if device == dev:
        device = dev
        print(f"Расположен {devices[device]['location']}")
        print(f"Вендор {devices[device]['vendor']}")
        print(f"Модель {devices[device]['model']}")
        print(f"Система (ios) {devices[device]['ios']}")
        print(f"IP адрес {devices[device]['ip']}")
# '&', '-', '^', '|' - выводят ошибку


"""
2) Есть словарь кодов товаров и словарь количества товара на складе, задача 
сопоставить два словаря и высчитать общее количество.
"""

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [{'quantity': 27, 'price': 42}],
    '23456': [{'quantity': 22, 'price': 510}, {'quantity': 32, 'price': 520}],
    '34567': [{'quantity': 2, 'price': 1200}, {'quantity': 1, 'price': 1150}],
    '45678': [{'quantity': 50, 'price': 100}, {'quantity': 12, 'price': 95},
              {'quantity': 43, 'price': 97}],
}

goods['Лампа'] = store['12345']
goods['Стол'] = store['23456']
goods['Диван'] = store['34567']
goods['Стул'] = store['45678']

for good, code in goods.items():
    quantity = 0
    price = 0
    for param in code:
        quantity += param['quantity']
        price += param['price']
    print(f'Продукт: {good}, Количество: {quantity}, Стоимость: {price}')
