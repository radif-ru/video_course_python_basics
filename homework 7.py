import random
import math

# homework 1
fruits1 = ['яблоки', 'груши', 'сливы', 'ананасы', 'апельсины', 'абрикосы']
fruits2 = ['мандарины', 'груши', 'персики', 'абрикосы', 'киви', 'бананы']

fruits = [fruit for fruit in fruits1 if fruit in fruits2]
print(fruits)

# homework 2
numbers = [random.randint(-100, 100) for number in range(100)]
print(f'Дано {len(numbers)} чисел: {numbers}')

numbers = [number for number in numbers if not number % 3 and number > 0 and number % 4]
print(f'Удовлетворяет условиям {len(numbers)} чисел: {numbers}')


# homework 3
numbers = [random.randint(-100, 100) for number in range(10)]
print(f'Дано {len(numbers)} чисел: {numbers}')


def get_numbers(n):
    return [round(math.sqrt(n[i]), 2) if n[i] > 0 else n[i] for i in range(len(n))]


print(f'Результат операции: {get_numbers(numbers)}')
print(f'Сравниваем с предыдущим значением: {numbers}')


# homework 4
def get_number(n):
    if n == 13:
        raise ValueError('Число равно 13!')
    else:
        return n**2


try:
    result = get_number(int(input('Введите число от 1 до 100. Ни в коем случае не воодите 13!\nВаше число: ')))
except ValueError as e:
    print('Что-то пошло не так...', e)
else:
    print()