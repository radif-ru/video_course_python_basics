# Мой метод, программа решает задачу математически максимально быстро

user_range = int(input('Выбери любой диапозон чисел от 0 до n (например 100) и загадай его, а я угадаю. '
                       '\nКакое наивысшее число n: '))

estimated_number = int(user_range / 2)
higher_range = user_range
lower_range = 0
user_answer = None

while user_answer != '=':
    user_answer = input(f'ТЫ ЗАГАДАЛ: {estimated_number}. '
                        f'\nЕсли я угадал набери: = \nЕсли число меньше: < \nЕсли число больше: > \nТвой ответ: ')

    if user_answer == '<':
        higher_range = estimated_number
        number_list = range(lower_range, higher_range)
        estimated_number = number_list[int(len(number_list) / 2)]
    elif user_answer == '>':
        lower_range = estimated_number + 1
        number_list = range(lower_range, higher_range)
        estimated_number = number_list[int(len(number_list) / 2)]
else:
    print('Ура! Сверхразум победил!')
exit()

# Версия преподавателя, программа решает задачу рандомно, иногда быстро, иногда долго

import random

min_number = 1
max_number = 100
result = None
while result != '=':
    number = random.randint(min_number, max_number)
    print(number)
    result = input('=> (загаданное число больше вашего) < ')
    if result == '>':
        min_number = number + 1
    elif result == '<':
        max_number = number - 1
print('Победа')
