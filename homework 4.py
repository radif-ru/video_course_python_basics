# homework 1
def person_info(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name.capitalize(), age, city.capitalize())


print(person_info('василий', 21, 'москва'))


# homework 2
def get_max(*args):
    return max(args)


print(get_max(234, 324, 123))


# homework 3
def player_attribute(name, health=100, damage=50):
    return {'name': name, 'health': health, 'damage': damage}


player = player_attribute(input('Введите имя: '))
enemy = player_attribute('Компутатор', 75, 45)


def attack(unit, target):
    target['health'] -= unit['damage']


attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)


# homework 4
def player_attribute(name, health=100, damage=50, armor=1.2):
    return {'name': name, 'health': health, 'damage': damage, 'armor': armor}


player = player_attribute(input('Введите имя: '))
enemy = player_attribute('Компутатор', 80, 45, 1.1)


def attack(unit, target, damage):
    target['health'] -= damage(unit['damage'], unit['armor'])


def get_damage(damage, armor):
    return int(damage/armor)


attack(enemy, player, get_damage)
print(player)

attack(player, enemy, lambda damage, armor: int(damage/armor))
print(enemy)

