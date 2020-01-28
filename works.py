
exit()
######################################################################################################
import os
import sys

name = sys.platform

for i in range(1, 6):
    new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
    os.mkdir(new_path)

exit()
######################################################################################################
import sys

# Путь до интерпретатора
print(sys.executable)
# Информация о платформе
print(sys.platform)

# Как питон находит модули?
print(sys.path)
print(type(sys.path))

sys.path.append('D:\\Python')
for p in sys.path:
    print(p)

# Выход и python
sys.exit()

print('Этот код мы уже не выполним')

######################################################################################################
import os

# имя операционной системы
print(os.name)

# текущая рабочая папка
print(os.getcwd())

# создаём новый путь
new_path = os.path.join(os.getcwd(), 'new_f')
print(new_path)
# создаём папку по новому пути
os.mkdir(new_path)

######################################################################################################
from hospital.h import get_main
from hospital.patients.index import get_index

get_main()
get_index()

######################################################################################################
from random import randint, choice, sample, shuffle

print(randint(0, 100))

players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(choice(players))
print(sample(players, 3))

cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
print(cards)
shuffle(cards)
print(cards)

######################################################################################################
import math

# 1. найти длину окружности с определенным радиусом
r = 100
print(2 * r * math.pi)

# 2. найти площадь окружности с определенным радиусом
print((r ** 2) * math.pi)
print((math.pow(r, 2)) * math.pi)

# 3. по координатам 2-х точек определить расстояние между ними
x1 = 10
y1 = 10
x2 = 50
y2 = 100
l = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(l)

# 4. найти факториал числа 9
print(math.factorial(9))

######################################################################################################
import math
import random as rd

print(help(math))
print(math.pi)
print(math.sin(38))

print(help(rd.randint))
print(rd.randint(1, 10))

from math import *
from random import randint

print(pi)
print(sin(30))

print(randint(1, 10))


######################################################################################################
def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result


numbers = list(range(1, 9))


def is_even(number):
    return number % 2 == 0


print(my_filter(numbers, is_even))
print(my_filter(numbers, lambda number: number % 2 != 0))
print(my_filter(numbers, lambda number: number > 4))

cities = [('Москва', 1000), ('Лас-Вегас', 500), ('Антверпен', 2000)]
print(sorted(cities), end='\n\n')


def by_count(city):
    return city[1]


print(sorted(cities, key=by_count))
print(sorted(cities, key=lambda city: city[1]), end='\n\n')

numbers = range(1, 9)


def is_even(number):
    return number % 2 == 0


result = filter(is_even, numbers)
print(result, '\n', list(result))

names = ['Max', 'Leo', 'Kate']
print(list(filter(lambda name: len(name) > 3, names)))
print(list(filter(lambda city: city[0].lower() == 'москва', cities)))
print(list(filter(lambda x: x[1] > 500, cities)))

print('\n', list(map(lambda x: x ** 2, numbers)))
print(list(map(lambda x: str(x), numbers)))


######################################################################################################


def greeting(say, *args):
    print(say, args)


greeting('Hello', 'Leo')
greeting('Hello', 'Leo', 'Max')
greeting('Hello', 'Leo')
greeting('Hello', 'Leo', 'Max', 'Kate')
print('\n')


def get_person(strong, builder, *args, sad, **kwargs):
    print(strong, builder, args, sad)
    print(kwargs)
    for k, v in kwargs.items():
        print(f'{k} {v}')


get_person('dadas', 'sadsad', '23', '2332', sad=[1, 2, 3], name='Leo', age=20, has_car=True)


def some_f():
    return 10


a = some_f
print(a, type(a), sep='  -->  ')
print(some_f, type(some_f), sep='  -->  ')
print('print(a())', type(print(a())), sep='  -->  ')

######################################################################################################


name = input('Как тебя зовут: ')
age = int(input('Сколько Вам лет: '))
# number_3 = int(input('Число 3'))

period = int(input('Период'))

print('Привет', name)

age_period = age + period
print('Через', period, 'лет Вам будет', age_period, sep=' / ')

# / в результате деления, тип данных всегда будет float
print(age / period, end=' / ')
print(type(age / period))
# // целая часть от деления, тип данных всегда будет int
print(age // period, end=' // ')
print(type(age // period))
# % остаток от деления, тип данных всегда будет int, пример 3%2 равно одна целая одна вторая
print(age % period, end=' % ')
print(type(age % period))
# возведение в степень **
print(age ** period, end=' ** ')
print(type(age ** period))

# сложные логические операции and, not, or
while name == 'инокентий':
    if name == 'парабола':
        break
    elif name == False:
        continue
    print('офкоз')
    if age == 18 and period != 0:
        print('так')
    elif not age:
        a = True
    else:
        a = 'тasafas'
else:  # выполнится после завершения цикла
    print('ehuuu в цикле break не было или мы в цикл не зашли')

print('\n\n\n')

print('Первая буква имени:', name[0], 'Последняя буква имени:', name[-1])
print('Срез со 2 по 3 букву:', name[1:3], 'Срез с начала по 2 букву:', name[:2], 'Срез со 2 буквы до конца:', name[1:])

print(name.isdigit())
print(help(str))

print('Привет %s тебе %d лет, а период %d' % (name, age, period))
print('Привет {} тебе {} лет, а период {}'.format(name, age, period))

top5 = 'Первые 5 мест на ссоревнованиях: 1. Пупкин 2. Петров 3. Харитонов 4.  Иванов 5. Степанов'
start = top5.find('1')
end = top5.find('4')

top3 = top5[start:end]

result = 'Поздравляем {}с успехом!'.format(top3.upper())
print(result)

winners = ['Max', 'Leo', 'Kate']

# простой перебор
for winner in winners:
    print(winner)

# используя range
for i in range(len(winners)):
    print(++i, ') ', winners[i], sep='')

# range
for number in reversed(range(1, 1000, 2)):
    print(number)

friend = {
    'name': 'Max',
    'age': 23
}

print(friend, type(friend), friend['age'], sep=', ')

friend['has_car'] = True
print(friend)

del friend['age']

friend['has_car'] = False
print(friend)

if 'has_car' in friend:
    print('Есть машина')

for key in friend.keys():
    print(key, friend[key], sep=' -> ')

for key in friend:
    print(key, friend[key], sep=' => ')

for val in friend.values():
    print(val)

# safasfafas
for item in friend.items():
    print(item)

for key, val in friend.items():
    print(key, val, sep=' > ', end='; ')

# множества

cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']

print('\n\n', type(cities), cities)

print(set(cities), type(set(cities)))

cities = {'Las Vegas', 'Paris', 'Moscow'}
print(cities)
cities.add('Burma')
print(cities)
cities.add('Moscow')
print(cities)

cities.remove('Las Vegas')
print(cities, len(cities))

print('Paris' in cities)

for city in cities:
    print(city)

# операции с множествами, работают как в математике
# Max взял
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
# Kate взяла
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

# какие вещи взяли супруги?
print(max_things | kate_things)
# какие вещи повторяются?
print(max_things & kate_things)
# какие вещи взял max, но не взяла kate
print(max_things - kate_things)
# какие вещи взяла kate, но не взял max
print(kate_things - max_things)
