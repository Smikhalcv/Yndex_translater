# Задача №1
# Нужно реализовать Польскую нотацию для двух положительных чисел. Реализовать нужно будет следующие операции:
#
# Сложение
# Вычитание
# Умножение
# Деление
# Например, пользователь вводит: + 2 2 Ответ должен быть: 4
#
# Задача №2
# С помощью выражения assert проверять, что первая операция в списке доступных операций (+, -, *, /). С помощью конструкций try/expcept
# ловить ошибки и выводить предупреждения Типы ошибок:
#
# Деление на 0
# Деление строк
# Передано необходимое количество аргументов
# и тд.
# Задача №3
# Расширить домашние задание из лекции 1.4 «Функции — использование встроенных и создание собственных» новой функцией, выводящей имена
# всех владельцев документов. С помощью исключения KeyError проверяйте, есть ли поле "name" у документа.

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }

#def polish_notation():
# try:
#     def polish_notation(operator, a, b):
#         value = input('Введите через пробел: операцию (+, -, *, /) и два положительных числа, над которыми она совершается - ')
#         value_list = value.split()
#         operator = value_list[0]
#         a = int(value_list[1])
#         b = int(value_list[2])
#         assert operator in ('+', '-', '*', '/'), 'Неверно введён оператор.'
#         if operator == '+':
#             return (a + b)
#         elif operator == '-':
#             return (a - b)
#         elif operator == '*':
#             return (a * b)
#         elif operator == '/':
#             return (a / b)
#     # except BaseException as f:
#     #     print(f'В коде ошибка - {f}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')

def polish_notation():
    try:
    # def polish_notation(operator, a, b):
    #     print('Введите через пробел: операцию (+, -, *, /) и два положительных числа, над которыми она совершается - ')
        value = input('Введите через пробел: операцию (+, -, *, /) и два положительных числа, над которыми она совершается - ')
        value_list = value.split()
        operator = value_list[0]
        a = int(value_list[1])
        b = int(value_list[2])
        assert operator in ('+', '-', '*', '/'), 'Неверно введён оператор.'
        if operator == '+':
            return (a + b)
        elif operator == '-':
            return (a - b)
        elif operator == '*':
            return (a * b)
        elif operator == '/':
            return (a / b)
        # else:
        #     print('Неверно введён оператор.')
    # except BaseException as f:
    #     print(f'В коде ошибка - {f}')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    except TypeError as f:
        print(f'Ошибка типа данных: {f}.')
    except IndexError:
        print('Недостаточное количество аргументов.')
    except ValueError:
        print('Неверный тип данных.')

polish_notation()

# #def name_documents(documents):
#     i = 0
#     a = 'name'
#     try:
#         for i in range(len(documents)):
#             print(documents[i][a])
#             i += 1
#     except KeyError:
#         print(f"У документа нет поля {a}!")

