import json
import os


def set_file(file):
    """Создает файл для пользователя"""
    usr = 'users'
    sec = file.split('.')
    jsn = '.json'
    if sec[-1] != 'json':
        filename = os.path.join(usr, sec[0] + jsn)
    else:
        filename = os.path.join(usr, sec[0])
    return filename


def get_stored_name(file):
    """Получает хранимое имя пользователя, если оно существует"""
    filename = set_file(file)
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username(file):
    """Запрашивает новое имя пользователя"""
    username = input("What's your name? ")
    filename = set_file(file)
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user(file):
    """Приветствует пользователя по имени"""
    username = get_stored_name(file)
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username(file)
        print("We will remember you when you will comeback, "
              + username + "!")


# file = input("Введите название файла:\n")
# greet_user(file)
