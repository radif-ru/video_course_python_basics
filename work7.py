is_has_name = True
name = 'Max' if is_has_name else 'Empty'
print(name)

is_has_name = False
name = 'Max' if is_has_name else 'Empty'
print(name)

is_one = False
number = 1 if is_one else 2
print(number)

is_russian = True
print('Привет' if is_russian else 'Hello')

is_russian = False
print('Привет' if is_russian else 'Hello')

word = 'Привет'
# мой метод
mod_word = ''
for i in range(len(word)):
    mod_word += f'{word[i].upper() if not i % 2 else word[i].lower()}'
print(mod_word)

# метод препода
result = []
for i in range(len(word)):
    letter = word[i]
    letter = letter.lower() if i % 2 else letter.upper()
    result.append(letter)
result = ''.join(result)
print(result)

####
password = 'secret'
print('Войти' if password == 'secret' else 'Вход запрещен')

# записать в список только положительные числа
numbers = [1, 2, 3, 4, 5, -1, -2, -3]

# через функцию filter
result = filter(lambda number: number > 0, numbers)
print(list(result))

# через генератор
result = [number for number in numbers if number > 0]
print(result)

# генератор словаря...
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

# классический способ
result = {}
for pair in pairs:
    key = pair[0]
    val = pair[1]
    result[key] = val
print(result)

# через генератор словаря
result = {pair[0]: pair[1] for pair in pairs}
print(result)

import random

numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

numbers = [1, 2, 3, -4]
numbers = [i ** 2 for i in numbers]
print(numbers)

names = ['Руслан', 'Дмитрий', 'Алексей', 'Андрей']
names = [name for name in names if name.startswith('А')]
print(names)

import math

if 1 > 2 and math.sqrt(-1):
    print('Ошибки не будет т.к. первое условие ложь')
print('Двигаемся дальше')

# if math.sqrt(-1) and 1 > 2:
#     print('Если поменять местами то будет ошибка')

# and - возвращается первая ложь
print([1] and [] and '' and 1)

# and - возвращается последняя истина
print([1] and 1 and 20 and 1.1)

if 2 > 1 or math.sqrt(-1):
    print('Ошибки не будет т.к. первое условие истина')

# if math.sqrt(-1) or 1 < 2:
#     print('Если поменять местами то будет ошибка')

# or - в отличии от and наоборот - возвращается первая истина
print(0 or [] or 8 or 5)

# or - в отличии от and наоборот -  возвращается последняя ложь
print(0 or [] or () or {})

import math

numbers = [4, 1, 2, 3, -4, -2, 7, 16]
# создать список, где квадратный корень меньше 2
numbers = [number for number in numbers if number > 0 and math.sqrt(number) > 2]
# ниже будет ошибка так как возможное ошибочное условие стоит первым и выдало ошибку
# numbers = [number for number in numbers if math.sqrt(number) > 2 and number > 0]
print(numbers)


def add_to_list(input_list=None):
    input_list = input_list or []
    # так выдаст ошибку при вызове без аргумента:
    # input_list = [] or input_list
    input_list.append(2)
    return input_list


print(add_to_list([0, 1]))
print(add_to_list())


import copy

a = [1, 2, [1, 2]]

b = copy.deepcopy(a)
b[2][1] = 200

print(a)
print(b)

# исключения
number = 0
try:
    result = 100/number
except ZeroDivisionError as e:
    print('Попытка деления на 0')
    print('Информация об исключении', e)
except Exception as e:
    print('Неизвестная ошибка')
    print('Информация об исключении', e)

number = int(input('Введите число: '))
try:
    result = 100/number
except:
    print('Попытка деления на 0')
else:
    print('Все хорошо ошибок не было')
finally:
    print('Что делаем когда есть ошибка и когда её нет')

print('Начало')
raise Exception('Что-то пошло не так')
print('Конец')
