# while True: print(eval(input('>>>')))

# class Item:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     def __add__(self, other):
#         if isinstance(other, Item):
#             return self.price + other.price
#         elif isinstance(other, int):
#             return self.price + other
#
# item_1 = Item('Видеокарта', 15000, 0.8)
# item_2 = Item('Процессор', 12000, 0.2)
#
# total_price = item_1 + 5000
# print(total_price)
#
# from tkinter import *
# import random
# window = Tk()
# window.geometry('600x600')
#
# class Fire:
#     image = PhotoImage(file = 'fire.png').subsample(5,5)
#     def __add__(self, other):
#         if isinstance(other, Earth):
#             return Clay
# class Water:
#     image = PhotoImage(file = 'water.png').subsample(5,5)
#     def __add__(self, other):
#         if isinstance(other, Wind):
#             return Aroma
# class Wind:
#     image = PhotoImage(file = 'wind.png').subsample(5,5)
#     def __add__(self, other):
#         if isinstance(other, Water):
#             return Aroma
# class Earth:
#     image = PhotoImage(file = 'ground.png').subsample(5,5)
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Clay
# class Clay:
#     image = PhotoImage(file = 'pottery.png').subsample(5,5)
#
#
# class Aroma:
#  image = PhotoImage(file='aroma.png').subsample(5, 5)
#
#
# canvas = Canvas(window, width=600, height=600)
# canvas.pack()
#
# elements = [Fire(), Water(), Wind(), Earth(),]
# for elem in elements:
#     canvas.create_image(random.randint(50, 550), random.randint(50, 550), image = elem.image)
#
# def move(event):
#     # print(event.x,event.y)
#     images_id = canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)
#     # print(images_id)
#     canvas.coords(images_id, event.x, event.y)
#
#     if len(images_id)==2:
#         elem_id_1, elem_id_2 = images_id[0], images_id[1]
#         element_1, element_2 = elements[elem_id_1-1], elements[elem_id_2-1]
#
#     new_element = element_1 + element_2
#     if new_element:
#         if new_element not in elements:
#             canvas.create_image(event.x, event.y, image = new_element.image)
#             elements.append(new_element)
#
# window.bind('<B1-Motion>', move)
# window.mainloop()

from pprint import pprint
from typing import Iterator
#
# print(__name__)
#
# goods = [
#             {
#                 'name': 'Iphone 14',
#                 'brand': 'Apple',
#                 'price': 1200,
#             },
#             {
#                 'name': 'Samsung Galaxy A53',
#                 'brand': 'Samsung',
#                 'price': 500,
#             },
#             {
#                 'name': 'REALME C25s',
#                 'brand': 'REALME',
#                 'price': 400,
#             }
#         ]
#
#
# if __name__ == '__main__':

    #-----------------------lambda---------------------
    # lambda аргументы: выражение
    #
    # + можно использовать в других встроенных функциях, можно вкладывать lambda в lambda
    # - нельзя использовать циклы, всё в одну строку
    #
    # def item_price(item):
    #     return item['price']
    #
    # pprint(sorted(goods, key=lambda item: item['price']))
    #
    # def double(x):
    #     return x*2
    # print(double(6))
    # print((lambda x: x*2)(8))
    #
    # print((lambda x: 'POSITIVE' if x >=0 else 'NEGATIVE')(-5))

    #---------------------filter----------------------------
    # filter(возвращающая bool функция, итерируемый объект фильтрации)

    # apple_list = filter(lambda item: item['brand'] == 'Apple', goods)
    # print(isinstance(apple_list, Iterator))
    # pprint(list(apple_list))

    ##Бонус

    # lst = [0, 1, False, 2, '', 3, 'a', 's', 34, None]
    # print(lst)
    # print(list(filter(None, lst)))


    #--------------------------map------------------------------
    #map(функция, итерируемый_объект, [итерируемый_объект_2, итерируемый_объект_3, ...])

    # numbers_list = ['1', '2', '3', '4', '215', '-98']
    #
    # print(list(map(int, numbers_list)))
    #
    # names_list = ['Даниил', 'Алиса', 'Геральт']
    # surnames_list = ['Старк', 'из Ривии', 'Растовый']
    # patronymic_list = ['Сергеевич', 'Петрович']
    #
    # full_names_list = list(map(lambda name, surname, patronymic: f'{name} {surname} {patronymic}', names_list, surnames_list, patronymic_list))
    # print(full_names_list)

    #------------------enumerate------------------
    # enumerate(итерируемый_объект, [start=0]) --> кортежи(счетчик, элемент)

    # indexed_list=[]
    # for i in enumerate(goods, start=1):
    #     print(i)
    #     indexed_list.append({i[0]:i[1]})
    # print()
    # pprint(indexed_list)

    #-------------------------zip---------------------------
    # zip(итерируемый_объект_1, итерируемый_объект_2, [итерируемый_объект_3, ....])--> кортежи

    # for name, surname, patronymic in zip(names_list, surnames_list, patronymic_list):
    #     print(f'{name} {surname} {patronymic}')
    #



# token = "vk1.a.YKX-sZVaFnobr1hdWJvlFfQUu1axlNHH1Z7GZkLOCRrhoZcRpjY0L0NRg1udCzKRnG9ydd5VQSv_ipp0Lcwx590EN2zYhITKseTUYNzaEU_JhxGnKUYjGlBGQglT6mjLbaC0grBDp98DI8k2SzCq5L6v98GGtMn7jx2bQfIs99NhcvCyb65TTG--EzV8NZVezPCj8stbrWyzKIapnpyGIg"
#
# import vk_api
# from vk_api.longpoll import VkEventType, VkLongPoll
# import random
# from course import get_course
# from wiki import get_wiki_article
#
# def main():
#     vk_session = vk_api.VkApi(token=token)
#     vk = vk_session.get_api()
#     longpoll = VkLongPoll(vk_session)
#     hello_msg = 'Привет! Я бот Ксюша, я могу выполнять следующие команды:\n' \
#                 '-к - курс валют,\n' \
#                 '-в "запрос" - запрос в википедии.'
#
#     for event in longpoll.listen():
#         if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#             msg = event.text.lower()
#             user_id = event.user_id
#             # print(f'{user_id}:{msg}')
#             random_id = random.randint(1, 9999999)
#             if msg[0:2] == '-к':
#                 response = '{0} рублей за 1 доллар \n' \
#                            '{1} рублей за 1 евро \n' \
#                            '{2} рублей за 10 юаней \n' \
#                            '{3} рублей за 1 фунт \n'.format(get_course('R01235'),
#                                                             get_course('R01239'),
#                                                             get_course('R01375'),
#                                                             get_course('R01035'))
#             elif msg.startswith('-в'):
#                 article = msg[2:]
#                 response = get_wiki_article(article)[:4000]
#             else:
#                 response = hello_msg
#             vk.messages.send(user_id = user_id, random_id = random_id, message = response)
# main()

# import requests
# import xml.etree.ElementTree as ET
# from contextlib import contextmanager
# from datetime import datetime
# URL = "http://www.cbr.ru/scripts/XML_daily.asp"
# # Нужно типо везти код валюты типо AUD И ВАМ ВЫВЕДЕТ СКОЛЬКО ОН СТОИТ
#
# valid_codes = ['AUD']
# @contextmanager
# def get_currency_rate(currency_id):
#     today = datetime.today().strftime("%d/%m/%Y")
#     url = f"{URL}?date_req={today}"
#     response = requests.get(url)
#     xml = ET.fromstring(response.content)
#     valute = xml.find(f"./Valute[CharCode='{currency_id}']")
#     if valute:
#         rate = float(valute.find('Value').text.replace(",", "."))
#         yield f"(1 шт.) {valute.find('Name').text} стоит(ят) {rate:.4f} руб."
#     else:
#         yield f"Ошибка: валюта {currency_id} не найдена"
# currency_id = input("Введите код валюты: ")
# if currency_id not in valid_codes:
#     print("Неверный код валюты")
# else:
#     with get_currency_rate(currency_id) as rate:
#         print(rate)
#
# class item:
#
#
#  def __init__(self, price, brand):
#   self.price = price
#
#
#   self.brand = brand
#
#
# def __repr__(self):
#  return self.brand
#
#
# items_list = [
#  item(1000, "Apple"),
#  item(1200, "Apple"),
#  item(900, "Samsung"),
#  item(700, "Samsung"),
#  item(660, "Xiaomi")
# ]
# print(items_list)
# for x in items_list: print(x.brand, x.price)
# result = list(filter(lambda x: x.brand == 'Apple', items_list))
# print(result)
# for x in result: print(x.brand, x.price)



# names_list = ['данил', 'артём', 'никита', 'влад']
# print([x[0].upper() + x[1:] for x in names_list])
# print([w.capitalize() for w in names_list])


# class Item:
#
#
#  def init(self, price, weight):
#   self.price = price
#
#
#
#
# def __sub__(self, other):
#  new_price = self.price - other.price
#  new_weight = self.weight - other.weight
#  return Item(new_price, new_weight)
#
#
# def __mul__(self, other):
#  new_price = self.price * other
#  new_weight = self.weight * other
#  return Item(new_price, new_weight)
#
#
# def __truediv__(self, other):
#  new_price = self.price / other
#  new_weight = self.weight / other
#  return Item(new_price, new_weight)
#
#
#
#
# item1 = Item (100,1)
# item2 = Item (50, 0.5)
#
# item3 = item1 - item2
# print(item3.price, item3.weight)
#
# item4 = item1 * 2
# print(item4.price, item4.weight)
#
# item5 = item1 / 2
# print(item5.price, item5.weight)

# class Year:
#
#
#  def __init__(self, days):
#   self.days = days
#
#
# @property
# def days(self):
#  return self.__days
#
#
# @days.setter
# def days(self, days):
#  if days == 366 or days == 365:
#   self.__days = days
#
#
# raise Exception('Некорректное значение')
#
# year = Year(365)
#
# year.days = (36)
#
# print(year.days)
#
#
#
#
# from pprint import pprint
#
#
# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         if value.strip() == '':
#             raise ValueError('name cannot be empty')
#         self._name = value
#
#     @name.deleter
#     def name(self):
#         del self._name
#
# pprint(Person.__dict__)
#
# person = Person('John')
#
# pprint(person.__dict__)
#
#
# del person.name

# class InfiniteIterator:
#  def __init__(self, start):
#   self.start = start
#
#  def __iter__(self):
#   return self
#
#  def __next__(self):
#   self.start += 1
#   return self.start - 1
#
#
#
# my_iterator = InfiniteIterator(0)
#
#
# for i in my_iterator:
#  print(i)
#  if i > 10:
#   break

# list_1 = []
#
# for i in range(5):
#  enter_a_name = input('Введите имя сотрудника: ')
#  enter_a_salary = int(input('Введите заработную плату сотрудника: '))
#  good_employee = bool(
#   input('Хорошо ли работал этот сотрудник? (введите True, если да и не заполняйте поле, если нет) - '))
#
#
#  class Employee:
#   def __init__(self, name=enter_a_name, salary=enter_a_salary, on_vacation=False, is_good_employee=good_employee):
#    self.name = name
#    self.salary = salary
#    self.on_vacation = on_vacation
#    self.is_good_employee = is_good_employee
#
#   def get_info(self):
#    return f'{self.name} получает в месяц {self.salary} рублей. В отпуске ли он? - {self.on_vacation}. Хорошо ли он работал? - {good_employee}'
#
#
#  dict_1 = {}
#  dict_1['name'] = enter_a_name
#  dict_1['good_job'] = good_employee
#  list_1.append(dict_1)
#
# for a in range(len(list_1) - 1, -1, -1):
#  if list_1[a]['good_job'] == False:
#   del list_1[a]
#
# print(list_1)

#
# import vk_api
# from vk_api.longpoll import VkLongPoll, VkEventType
# import random
# import requests
#
# token = ""
# vk_session = vk_api.VkApi(token=token)
# vk = vk_session.get_api()
# longpoll = VkLongPoll(vk_session)
#
#
# def get_largest_planet():
#  api_url = "https://swapi.dev/api/planets"
#  response = requests.get(api_url)
#  data = response.json()
#  largest = data["results"][0]
#  for planet in data["results"]:
#   if int(planet["diameter"]) > int(largest["diameter"]):
#    largest = planet
#  return largest["name"]
#
#
# for event in longpoll.listen():
#  if event.type == VkEventType.MESSAGE_NEW and event.to_me:
#   msg = event.text.lower()
#   user_id = event.user_id
#   random_id = random.randint(1, 9999999)
#   if msg == "планеты":
#    response = f'Самая большая планета - {get_largest_planet()}'
#   else:
#    response = "Неизвестная команда. Вот что я умею: планеты: выдать планету с максимальным диаметром"
#   vk.messages.send(peer_id=user_id, random_id=random_id, message=response)

# import requests
#
#
# def get_starships():
#  response = requests.get("https://swapi.dev/api/starships/")
#  return response.json()
#
#
# def handle_message(message):
#  if message == "корабли":
#   starships = get_starships()["results"]
#   fastest_starship = max(starships, key=lambda x: int(x["max_atmosphering_speed"]))
#   response = f'Максимальная скорость звездного корабля {fastest_starship["name"]} - {fastest_starship["max_atmosphering_speed"]} км/ч.'
#  else:
#   response = "Я не понимаю, что вы хотите."
#  return response
# message = input("Введите сообщение: ")
# response = handle_message(message)
# print(response)
#
# import sqlite3
# from pprint import pprint
#
# # try:
# #     connection = sqlite3.connect('data.db')
# #     cursor = connection.cursor()
# # except sqlite3.DatabaseError:
# #     print('Ошибка при подключении в БД')
# # finally:
# #     connection.close()
#
# def create_new_table(cursor):
#     command = """
#         CREATE TABLE IF NOT EXISTS users(
#         id INTEGER PRIMARY KEY,
#         name TEXT,
#         surname TEXT,
#         gender TEXT
#         );
#         """
#     cursor.execute(command)
#
# def get_users_list(cursor):
#     command = """
#         SELECT * FROM users;
#         """
#     result = cursor.execute(command)
#     users = result.fetchall()
#     pprint(users)
#
# def get_gender(cursor,gender_id ):
#     command = """
#         SELECT * FROM id = 'муж.';
#         """
#     result = cursor.execute(command,gender_id )
#     genders = result.fetchall()
#     pprint(genders)
#
# def add_user(cursor, user):
#     command = """
#             INSERT INTO users(name, surname, gender) VALUES (?,?,?);
#             """
#     cursor.execute(command, (user.name, user.surname, user.gender))
#
# def update_user_name(cursor, name, user_id):
#     command = """
#                 UPDATE users SET name = ? WHERE id = ?;
#                 """
#     cursor.execute(command, (name, user_id))
#
#
# def delete_users(cursor):
#     command = """
#                 DELETE FROM USERS WHERE id = 2
#                 """
#     cursor.execute(command)
#
# class User:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#
# if __name__ == '__main__':
#     with sqlite3.connect('data.db') as cursor:
#         create_new_table(cursor)
#         delete_users(cursor)
#         add_user(cursor, User('Михаил', 'Михайлов', 'муж.'))
#         add_user(cursor, User('Bruce', 'Wayne', 'муж.'))
#         add_user(cursor, User('Elizaveta II', 'Windsor', 'жен.'))
#         get_users_list(cursor)
#         # get_user(cursor,)
#         update_user_name(cursor, 'Елизавета 2', '3')
#
# test_path = C:\test

import os


# import os
#
# current_path = os.path.abspath(__file__)
# parent_path = os.path.join(current_path, '..')
# # parent_path = os.path.split(current_path)
# print(parent_path)

# def recurs(count):
#     print(count)
#     if count == 5:
#         return
#     recurs(count+1)
#     print(count)
#
# recurs(0)
# tab = ''
# def get_all_files(path):
#     global tab
#     for i_name in os.listdir(path):
#         new_path = os.path.join(path, i_name)
#         if os.path.isdir(new_path):
#             print(tab + 'Папка', i_name)
#             tab += '\t'
#             get_all_files(new_path)
#         else:
#             print(tab + '-', i_name)
#     tab = tab[1:]
#
#
# get_all_files(test_path)

# generator_1 = (x ** 2 for x in range (1000000))
#
# print(generator_1)
#
#
#
#
# def generator_2():
#     for x in range (1000000):
#         yield x ** 2
# print(generator_2())

# while True: print(eval(input('>>>')))
# class Item:
#     def init(self, price, weight):
#
#         self.price = price
#         self.weight = weight
#
#
#
# def __sub__(self, other):
#     new_price = self.price - other.price
#     new_weight = self.weight - other.weight
#     return Item(new_price, new_weight)
#
#
# def __mul__(self, other):
#     new_price = self.price * other
#     new_weight = self.weight * other
#     return Item(new_price, new_weight)
#
#
# def __truediv__(self, other):
#     new_price = self.price / other
#     new_weight = self.weight / other
#     return Item(new_price, new_weight)
#
# def __add__(self, other):
#     if isinstance(other, Item):
#             return self.price + other.price
#     elif isinstance(other, int):
#      return self.price + other
#
# item_1 = Item('Видеокарта', 15000, 0.8)
# item_2 = Item('Процессор', 12000, 0.2)
# total_price = item_1 + 5000
# print(total_price)
#
# def strcounter(s):
#     for lit in s:
#         counter = 0
#         for sub_lit in s:
#           if lit == sub_lit:
#               counter +=1
#               print(lit,counter)
#
# strcounter('aaabcd')
#


# def strcounter(s):
#     for lit in set(s):

# s = 'aasddfg'
# print(list(s))
# print(set(s))
#
# def strcounter(s):
#     for lit in set(s):
#         counter = 0
#         for sub_lit in s:
#             if lit == sub_lit:
#                 counter += 1
#             print(lit,counter)
#
# strcounter('aaabcdddd')
#
# def strcounter(s):
#     lits_counter = {}
#     for lit in s:
#         lits_counter[lit] = lits_counter.get(lit,0) + 1
#     for lit, counter in lits_counter.items():
#         print(lit,counter)
#
# strcounter('aaaddfghhhhhhhhj')
#



# def slova():
#     s = in    name: str
    surname:str
    salary:int
    position:str












































































































