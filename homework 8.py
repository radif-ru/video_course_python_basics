import sys
from work8_core import create_file, create_folder, get_list, delete_file, copy_file, save_info, \
    change_dir, guess_the_number


save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо ввести название команды, список команд можно посмотреть набрав команду - help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название удаляемого файла или папки')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('В параметрах должны быть названия копируемого файла/папки и новой копии файла/папки')
        else:
            copy_file(name, new_name)
    elif command == 'ch':
        try:
            path = sys.argv[2]
        except IndexError:
            print('Отсутствует путь')
        else:
            change_dir(path)
    elif command == 'guess_the_number':
        try:
            guess_the_number()
        except ValueError:
            print('Ошибка вводимых данных')
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')

save_info('Конец')
