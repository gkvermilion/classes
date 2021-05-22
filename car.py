class Car():
    """Simple car model"""

    def __init__(self, make, model, year):
        """initialises car attributes"""
        self.make = make
        self.model = model
        self.year = year
        # значение по умолчанию
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns formatted description"""
        long_name = str(self.year) + ' ' + self.make + ' ' + \
                    self.model
        return long_name.title()

    def read_odometer(self):
        """Print car's odometer"""
        print(f'This car has {str(self.odometer_reading)} '
              f'kilometers on it.')

    def update_odometer(self, mileage):
        """Sets new value for odometer"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print('Odometer value has changed!')
            Car.read_odometer(self)
        else:
            print('You can\'t roll back an odometer!')
            Car.read_odometer(self)

    def increment_odometer(self, kilometers):
        """Increases odometer's value"""
        if kilometers < 0:
            print('You can\'t roll back an odometer!')
            Car.read_odometer(self)
        else:
            self.odometer_reading += kilometers
            Car.read_odometer(self)

    def fill_gas_tank(self):
        """fills gas tank"""
        print('Full gas')


my_new_car = Car('mercedes', 'cls', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 2360
my_new_car.read_odometer()

my_new_car.update_odometer(4500)

my_new_car.update_odometer(1234)

my_used_car = Car('honda', 'civic', 2001)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(3500)
my_used_car.read_odometer()

my_used_car.increment_odometer(3500)
my_used_car.read_odometer()

my_used_car.increment_odometer(-100)
my_used_car.read_odometer()


# my_used_car.odometer_reading = 2500
# my_used_car.read_odometer()


class Battery():
    """Simple battery model"""

    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print('This car has a ' + str(self.battery_size) +
              '-kwh battery.')

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора"""
        if self.battery_size == 70:
            range = 240
            message = "This car can go approximately " + \
                      str(range)
            message += " kilometers on a full charge"
            print(message)
        elif self.battery_size == 85:
            range = 270
            message = "This car can go approximately " + \
                      str(range)
            message += " kilometers on a full charge"
            print(message)
        else:
            print("Can't calculate the distance")


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электрокаров"""

    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя.
        Затем инициалирует атрибуты для электрокара
        """
        super().__init__(make, model, year)
        # self.battery_size = 70
        self.battery = Battery()

    # def describe_battery(self):
    #   """Выводит информацию о мощности аккумулятора"""
    #  print('This car has a ' + str(self.battery_size) +
    #       '-kwh battery.')

    def fill_gas_tank(self):
        """У электрокара нет бензобака"""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.battery_size = 85
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.battery_size = 120
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
