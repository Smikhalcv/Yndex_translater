# Задача №1
# Необходимо реализовать менеджер контекста, печатающий на экран:
#
# Время запуска кода в менеджере контекста;
# Время окончания работы кода;
# Сколько было потрачено времени на выполнение кода.
# Задача №2
# Придумать и написать программу, использующая менеджер контекста из задания 1. Если придумать не получиться, использовать
# программу из предыдущих домашних работ.

import datetime
from pprint import pprint

class MyOpen:

    def __init__(self, path, method):
        self.path = path
        self.method = method

    def __enter__(self):
        self.file = open(self.path, self.method, encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.closed

print(__name__)
t1 = datetime.datetime.now()

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
        print('Неверное указано количестко блюд.')

pprint(get_shop_list_by_dishes("Запеченный картофель", "Омлет", 5))

t2 = datetime.datetime.now()
t3 = t2 - t1

print(f'Время начала работы кода {t1}')
print(f'Время конца работы кода {t2}')
print(f'Время выполнения кода {t3}')
if __name__ == '__main__':

    with MyOpen('testfile.txt', 'w') as test_file:
        for i in (get_shop_list_by_dishes("Запеченный картофель", "Омлет", 5)).keys():
            test_file.write(f'{i} : {str(get_shop_list_by_dishes("Запеченный картофель", "Омлет", 5)[i])}\n')
        test_file.write(f'Время начала работы кода {t1} \n')
        test_file.write(f'Время конца работы кода {t2} \n')
        test_file.write(f'Время выполнения кода {t3} \n')


