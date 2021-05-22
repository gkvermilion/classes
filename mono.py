class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


a = Cat()
b = Cat()
print(a.__dict__)
print(b.__dict__)
a.breed = 'siam'
print(a.__dict__)
print(b.__dict__)
b.name = 'Tony'
print(a.__dict__)
print(b.__dict__)
