# Необходимо написать программу для кулинарной книги.
#
# Список рецептов должен храниться в отдельном файле в следующем формате:
#
# Название блюда
# Количество ингредиентов в блюде
# Название ингредиента | Количество | Единица измерения
# Название ингредиента | Количество | Единица измерения
# ...
# Пример(файл в папке 2.4.files):
#
# Омлет
# 3
# Яйцо | 2 | шт
# Молоко | 100 | мл
# Помидор | 2 | шт
#
# Утка по-пекински
# 4
# Утка | 1 | шт
# Вода | 2 | л
# Мед | 3 | ст.л
# Соевый соус | 60 | мл
#
# Запеченный картофель
# 3
# Картофель | 1 | кг
# Чеснок | 3 | зубч
# Сыр гауда | 100 | г
#
# Фахитос
# 5
# Говядина | 500 | г
# Перец сладкий | 1 | шт
# Лаваш | 2 | шт
# Винный уксус | 1 | ст.л
# Помидор | 2 | шт
# В одном файле может быть произвольное количество блюд.
# Читать список рецептов из этого файла.
# Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.
# Задача №1
# Должен получится следующий словарь
#
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
# Задача №2
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
#
# get_shop_list_by_dishes(dishes, person_count)
# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова
#
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:
#
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
# Обратите внимание, что ингредиенты могут повторяться

from pprint import pprint

def def_cook_book():
    with open('recipes.txt', encoding='utf-8-sig') as f:
        cook_book = {}
        while True:
            cook = f.readline().strip()
            cook_book[cook] = []
            count = f.readline().strip()
            i = 0
            while i < int(count):
                a = f.readline().strip().split(' | ')
                cook_book[cook].append({'ingredient_name': a[0], 'quantity': a[1],'measure': a[2]})
                i += 1
            if f.readline() == '\n':
                continue
            else:
                break
        return cook_book

def get_shop_list_by_dishes(*order, cook_book = def_cook_book()):
    try:
        list_order = list(order)
        person_count = int(list_order[-1])
        del(list_order[-1])
        order = {}
        ingredients = []
        for i in list_order:
            y = 0
            for y in range(len(cook_book[i])):
                ingredients.append(cook_book[i][y])
                y += 1
        i = 0
        for i in range(len(ingredients)):
            if ingredients[i]['ingredient_name'] not in list(order.keys()):
                order[ingredients[i]['ingredient_name']] = {'measure': ingredients[i]['measure'],
                                                            'quantity': int(ingredients[i]['quantity']) * person_count}
            else:
                order[ingredients[i]['ingredient_name']]['quantity'] += int(ingredients[i]['quantity']) * person_count
            i += 1
        return order

    except KeyError:
        print('Таких блюд нет в меню.')
    except ValueError:
        print('Неверное указано поличестко блюд.')

pprint(get_shop_list_by_dishes('Запеченный картофель', 2))