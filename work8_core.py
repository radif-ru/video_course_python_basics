import os
import shutil
import datetime
import random


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def change_dir(path):
    os.chdir(os.path.abspath(path))


def guess_the_number():
    min_number = 1
    max_number = 100
    result = None
    while result != '=':
        number = random.randint(min_number, max_number)
        print(number)
        result = input('= (я угадал) \n> (загаданное число больше вашего) \n< (загаданное число меньше вашего)')
        if result == '>':
            min_number = number + 1
        elif result == '<':
            max_number = number - 1
    print('Победа')


if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_folder('new_f1')
    get_list()
    get_list(True)
    delete_file('new_f1')
    delete_file('text.dat')
    create_folder('new_f')
    copy_file('new_f', 'new_2')
    create_file('text.dat')
    copy_file('text.dat', 'text2.dat')
    save_info('abc')
    print(os.getcwd())
    working_directory('modules')
    print(os.getcwd())
    working_directory('..\..')
    print(os.getcwd())
    guess_the_number()