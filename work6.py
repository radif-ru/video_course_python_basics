f = open('first.txt', 'w')

f.write('Hello\n')
f.write('World\n')

f.writelines(['Hello\n', 'Python\n'])

f = open('first.txt', 'r')

# print(f.read())

# for line in f:
#     print(line.replace('\n', ''))

print(f.readlines())

f.close()

with open('first.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))

print('end')

##### байты
s = 'Hello world'
sb = b'Hello bytes'

print(s, type(s))
print(sb, type(sb))

print(s[1])
print(sb[1])

print(s[1:3])
print(sb[1:3])

for item in sb:
    print(item)


sb = b'Ad'
# по ascii таблице A = 65, d = 100
print(sb[0], sb[1])

s = 'Hello world'
sb = s.encode('ascii')
print(sb, type(sb))

s = 'Hello world Мир'
sb = s.encode('utf-8')
print(sb, type(sb))

s = sb.decode('utf-8')
print(s, type(s))

# файлы с байтами

with open('bytes.txt', 'wb') as f:
    f.write(b'Hello bytes')

with open('bytes.txt', 'r', encoding='ascii') as f:
    print(f.read())

with open('bytes.txt', 'wb') as f:
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

with open('bytes.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# чтение
with open('bytes.txt', 'wb') as f:
    str = 'Привет мир'
    f.write(str.encode('utf-8'))
# то же самое:
with open('bytes.txt', 'w', encoding='utf-8') as f:
    f.write('Привет мир')


with open('bytes.txt', 'rb') as f:
    result = f.read()
    print(result)
    print(type(result))
    s = result.decode()
    print(s)

# запись и чтение обЪекта в файл
person = {'name': 'Max', 'phones': [123, 345]}
# запись
with open('person.dat', 'wb') as f:
    name = person['name']
    f.write(f'{name}\n'.encode('utf-8'))
    phones = person['phones']
    for phone in phones:
        f.write(f'{phone}\n'.encode('utf-8'))

print('объект записан')
# чтение
with open('person.dat', 'rb') as f:
    result = f.readlines()

person = {}
person['name'] = result[0].decode('utf-8').replace('\n', '')

phones = []
for bphone in result[1:]:
    phones.append(bphone.decode('utf-8').replace('\n', ''))
    print(person)

# запись и чтение обЪекта в файл с помощью pickle

import pickle

person = {'name': 'Max', 'phones': [123, 345], 'age': 20}

with open('person.dat', 'wb') as f:
    pickle.dump(person, f)

print('Объект записан')

with open('person.dat', 'rb') as f:
    pickle.load(f)

print(person)

# работа с json

import json

friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 234]},
    {'name': 'Leo', 'age': 33},
    ['asdasdas', 214124],
    'adadad',
    1234,
    True
]
print(friends)
print(type(friends))

json_friends = json.dumps(friends)
print(json_friends)
print(type(json_friends))

friends = json.loads(json_friends)
print(friends)
print(type(friends))

# работа с json и файлом

friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 234]},
    {'name': 'Leo', 'age': 33},
    ['asdasdas', 214124],
    'adadad',
    1234,
    True
]

with open('friends.json', 'w') as f:
    json_friends = json.dump(friends, f)

with open('friends.json', 'r') as f:
    friends = json.load(f)

print(friends)
print(type(friends))


#
import json

favourite_tracks = [
    {'name': 'Вечная любовь', 'artist': 'Агата Кристи'},
    {'name': 'Angel', 'artist': 'Massive Attack'},
    {'name': 'Jamming', 'artist': 'Bob Marley'}
]

with open('tracks.json', 'w', encoding='utf-8') as f:
    json.dump(favourite_tracks, f)

print('Выполнено')