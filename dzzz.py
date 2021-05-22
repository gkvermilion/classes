from random import randint


def build_profile(first_name, last_name, **values):
    '''builds a profile'''
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in values.items():
        profile[key] = value
    return profile


def unique_id(profile):
    '''generates unique id'''
    id = {}
    val_name = 'id' + ''.join([str(randint(1, 99999999))])
    id[val_name] = profile
    return id


filename = 'database.txt'


def append_file(var):
    """adds data of user to database"""
    with open(filename, 'a') as file_object:
        file_object.write(str(var) + '\n')
