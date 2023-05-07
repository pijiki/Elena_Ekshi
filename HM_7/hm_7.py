import sys
import logging  # Загрузка библиотеки

# FORMAT = '%(asctime)s, ERROR %(message)s'
# logging.basicConfig(
#     filename='my_error.log',
#     format=FORMAT)  # Файл появится в том каталоге, где запущен скрипт
# logger = logging

"""break, continue, pass"""

"""
1) Есть список list1 = [i for i in range(100)], создайте новый список с 
пробросом каждого пятого элемента (используйте continue)
"""

# list1 = [i for i in range(100)]
# list2 = []
# for i in range(len(list1)):
#     if i % 5 != 0:
#         list2.append(i)
#     else:
#         continue
# print(list2)


"""
2) Напишите скрипт который будет работать циклично в интерактивном режиме, 
скрипт должен запрашивать имя пользователя, если пользователь не вводя имя 
нажмет на Enter то скрипт должен завершиться (используйте break)
"""

# while True:
#     str1 = input('Введите ваше имя или Enter: ')
#     if str1 == '':
#         break

"""
3) Есть список: list1 = [‘micros’, ‘python’, ‘linux’, ‘windows’, ‘bobo’], из 
него составить новый список, но без буквы ‘i’, результат: list2 = [‘mcros’, 
‘python’, ‘lnux’, ‘wndows’, ‘bobo’] (используйте pass)
"""

# list1 = ['micros', 'python', 'linux', 'windows', 'bobo']


# list2 = []
# list3 = []
#
# for i in list1:
#     c = list(i)
#     # print(i)
#     for v in c:
#         print(v)
#         if v != 'i':
#             list2.append(v)
#         elif v == 'i':
#             pass
# print(list2)


"""
Try/except/finally/else
"""

"""
1) Напишите программу, которая запрашивает ввод двух значений. Если хотя бы 
одно из них не является числом, то должна выполняться конкатенация, то есть 
соединение, строк. В остальных случаях введенные числа суммируются.
"""
# while True:
#     num1 = input('Первое значение: ')
#     if not num1:
#         break
#     num2 = input('Второе значение: ')
#     if not num2:
#         break
#
#     try:
#         num1, num2 = int(num1), int(num2)
#         print(num1 + num2)
#     except ValueError as error:
#         logger.error(error)
#         print(num1 + num2)
#     except TypeError as error:
#         logger.error(error)
#         print(num1 + num2)


"""
2) Есть список: list1 = [1, ‘a’, 3, ‘b’, 5, ‘6’, 7, ‘8’, 9, ‘c’], необходимо 
разделить на два списка, в первом только цифровые значения, а во втором только 
строки.
"""
#
# list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
# list2 = []
# list3 = []
#
# for i in list1:
#     try:
#         i = int(i)
#         if type(i) == int:
#             list2.append(i)
#     except ValueError as error:
#         logger.error(error)
#         list3.append(i)
# print(list2)
# print(list3)


"""
3) Тот же самый пример, с сообщением после каждой итерации о том, что элемент N 
добавлен.
"""
#
# list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
# list2 = []
# list3 = []
#
# for i in list1:
#     try:
#         i = int(i)
#         if type(i) == int:
#             list2.append(i)
#             print(f'В list2 добавлен элемент {i}')
#
#     except ValueError as error:
#         logger.error(error)
#         list3.append(i)
#         print(f'В list3 добавлен элемент {i}')
#     print(f'list2={list2};', end=' ')
#     print(f'list3={list3}')


"""
4) Приведенный ниже код назначает 5-ю букву каждого слова в food новый список 
fifth. Однако код в настоящее время выдает ошибки. Вставьте предложение 
try/except, которое позволит запустить код и создать список 5-й буквы в каждом 
слове. Если слово недостаточно длинное, оно не должно ничего выводить. 
Примечание. pass — Оператор является нулевой операцией; ничего не произойдет 
при его выполнении.
"""
#
# food = [
#     "chocolate", "chicken", "corn", "sandwich",
#     "soup", "potatoes", "beef", "lox", "lemonade"
# ]
# fifth = []
# for x in food:
#     try:
#         fifth.append(x[4])
#     except IndexError as error:
#         logger.error(error)
#         pass
# print(fifth)


"""
5) Приведенный ниже код делит значения элемента на самого себя, но вылетает с 
ошибками, необходимо учесть все типы ошибок и дописать код (условия цикла 
менять нельзя, использовать полный синтаксис try/except/else)
"""
#
# my_list = [2, "C", 10, "20", "micros", 50, 0, '0', '30']
#
# for index in range(len(my_list) + 5):
#     try:
#         if type(my_list[index]) == str:
#             my_list[index] = int(my_list[index])
#             print(f"Ошибка ValueError с элементом: '{my_list[index]}' так как тип элемента <class 'str'>")
#             print(f'{my_list[index]} / {my_list[index]} = {my_list[index] / my_list[index]}')
#             print(f"Но я сконвертировал значение '{my_list[index]}' в число и результат уже распечатал")
#         else:
#             print(f'{my_list[index]} / {my_list[index]} = {my_list[index] / my_list[index]}')
#             print(f'Всё получилось с первой попытки так как элемент {my_list[index]} является числом')
#
#     except ValueError as error:
#         logger.error(error)
#         print(f"Ошибка ValueError с элементом: '{my_list[index]}' так как тип элемента <class 'str'>")
#
#     except ZeroDivisionError as error:
#         logger.error(error)
#         print('На ноль делить нельзя')
#     except IndexError as error:
#         logger.error(error)
#         print(f'Список оказался слишком мал, индекс под номером {index} пуст')

"""
6) Дописать код (нельзя использовать просто except)
"""
#
# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
#
# try:
#     search_key = "non-existent key"
#     print(my_dict[search_key])
# except KeyError as error:
#     logger.error(error)
#     print("Сорян, 'non-existent key' это не правильный ключ!")


"""
7) Замените первый if на try/except/else
"""
# try:
#     while True:
#         city = input('Введите город: ')
#
#         if len(sys.argv) < 2:
#             city = sys.argv[1]
#             city = city.lower()
#         elif city == '':
#             break
# except IndexError:
#     pass
# # except SystemExit:
# #     print("Вы не указали название города")
# #     print("Try again")
# #     exit()
#
#
#
#
# if city == "tashkent"[0:len(city)]:
#     print("В Ташкенте тепло и солнечно")
# elif city == "london"[0:len(city)]:
#     print("В Лондоне пасмурно и сыро")
# elif city == "moscow"[0:len(city)]:
#     print("В Москве идёт сильный дождь")
# elif city == "paris"[0:len(city)]:
#     print("погода для романтики")
# elif city == "rio de janeyro"[0:len(city)]:
#     print("В Рио постоянно карнавалы")
#
# else:
#     print("прогноз не ясен, карантин")


"""
8) Следующий код работает отлично, если пользователь вводит цифровое значение, 
но всегда есть НО:
"""

# while True:
#     a = 0
#
#     try:
#         min_num = int(input("Введите первое число: "))
#         if min_num == 100:
#             break
#         max_num = int(input("Введите второе число: "))
#         if min_num > max_num:
#             print('Первое число должно быть меньше второго.')
#             print('Попробуйте еще раз.')
#
#         for i in range(min_num, max_num + 1):
#             print(f"Квадрат числа {i} равен {i * i}")
#         a += 1
#         if a >= 1:
#             print('Если хотите выйти, то введите 100.')
#     except ValueError as error:
#         logger.error(error)
#         print('Вы ввели не число')
#         print('Исправьте')


"""
9) Ловить ошибки это конечно здорово, но уметь логировать их и записывать в 
файл еще лучше, задача разобраться со стандартной библиотекой logging.
"""
"""
a) Найдите способ, чтобы можно было добавить время ошибки:
"""
#
# try:
#     1 / 0
# except ZeroDivisionError as error:
#     logger.error(error)

"""
b) Ко всем предыдущим примерам добавить логирования в файл
"""

"""
Работа с файлами
"""

"""
1) Откройте файл mbox-short.txt, “прочитайте” каждую строку в этом файле и 
найдите строки, соответствующие данной: “From Stephen.marquard@uct.ac.za Sat 
Jan 5 09:14:16 2008” . Затем распечатайте все ВХОДЯЩИЕ email адреса и их общее 
количество. Для решения данной задачи используйте методы строк. (используйте 
with open)
"""

# message = []
# with open('txt/mbox-short.txt', mode='r', encoding='UTF-8') as file:
#     for line in file:
#         if line.startswith('From '):
#             list1 = line.split()[1]
#             print(list1)
#             message.append(list1)
#     print(f'Количество входящих писем: {len(message)}')


"""
2) Откройте файл romeo.txt. “Прочитайте” в нем каждую строку. Получите 
отдельные слова из каждой строки, после чего составьте список слов. В списке 
слова не должны дублироваться. После чего распечатайте список, в котором все 
слова будут отсортированы в алфавитном порядке. (используйте open)
"""

# 1 способ:

# file = open('txt/romeo.txt', mode='r', encoding='UTF-8')
# content = set(file.read().split())
# print(list(sorted(content)))
# file.close()

# 2 способ:

# list1 = []
# file = open('txt/romeo.txt', mode='r', encoding='UTF-8')
#
# for line in file:
#     content = line.strip().split()
#     for word in content:
#         list1.append(word)
# set1 = set(list1)
# print(list(sorted(set1)))
#
# file.close()


"""
3) Напишите код программы, которая будет открывать файл «article.txt» и 
выводить на печать построчно последние строки в количестве lines (число которую 
можно запросить у пользователя). Число должно быть положительным (используйте 
with open)
"""


# list1 = []
#
# with open('txt/article.txt', encoding='UTF-8') as file:
#
#
#     for line in file:
#         content = line.strip()
#         # print(content)
#         list1.append(content)
# str1 = int(input('Сколько последних строк распечатать: '))
# # print(len(list1))
# print(f'{str(list1[str1::-1])}')

class Network_Range:
    # ip = input('Ведите ip-адрес: ')
    ip = '192.168.100.157/30'
    ip_mask = int(ip.split('/')[1])
    ip_network = ip.split('.')

    def __init__(self):
        self.k = None
        self.n = None
        self.ip2 = None
        self.ip1 = None
        self.set = None
        self.ip = self.ip_mask
        self.ip_network = self.ip_network
        self.list1 = [128, 192, 224, 240, 248, 252, 254, 255]

    def mask(self):
        # ip = int(self.ip.split('/')[1])
        self.ip1 = self.ip_mask % 8
        self.ip2 = self.ip_mask // 8

        for _ in range(self.ip2):
            i = 255
            print(i, end='.')
        # print(self.list1[self.ip1 - 1], end='')
        if self.ip2 == 0:
            print(f'.0.0.0 Mask', end='')
        elif self.ip2 == 1:
            print(f'.0.0 Mask', end='')
        elif self.ip2 == 2:
            print(f'.0 Mask', end='')
        elif self.ip2 == 3:
            print(f'{self.list1[self.ip1]} Mask', end='')

    def step(self):
        f = 0
        self.set = (32 - self.ip)

        for i in range(-1, self.set-1):
            f = 2 ** i
            f += f
        self.n = f + 2
        return self.n

    def network_address(self):
        try:
            self.k = self.ip_network[self.ip2]
            if self.k < self.n:
                return self.k == 0
            else:
                return int(self.k) // self.n * self.n
        except AttributeError:
            self.k = int(self.ip_network[3].split('/')[0])
            return self.k // self.n * self.n


mask = Network_Range()
print(mask.ip_network)
mask.mask()
print(f'\n{mask.step()}')
print(mask.network_address())
# i = 0
# for i in range(-1, 2-1):
#     f = 2 ** i
#     f += f
#     print(f)
# n = f + 1
# print(int(n))


