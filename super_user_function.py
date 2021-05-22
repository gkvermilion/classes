import json

def get_stored_name():
    """Получает хранимое имя пользователя, если оно существует"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя"""
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Приветствует пользователя по имени"""
    username = get_stored_name()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We will remember you when you will comeback, "
              + username + "!")


greet_user()