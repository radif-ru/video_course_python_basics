import json
import pickle

# homework 1 запись в файл
my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [{'name': 'Делать панк-рок', 'year': 2016},
               {'name': 'Шапито', 'year': 2014}]}

print(json.dumps(my_favourite_group), type(json.dumps(my_favourite_group)), sep='\n')
with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_favourite_group, f)

print(pickle.dumps(my_favourite_group), type(pickle.dumps(my_favourite_group)), sep='\n')
with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)


# homework 2 чтение из файла

with open('group.json', 'r', encoding='utf-8') as f:
    result = json.load(f)
print(result, type(result), sep='\n')

with open('group.pickle', 'rb') as f:
    result = pickle.load(f)
print(result, type(result), sep='\n')
