from car import ElectricCar

new_tesla = ElectricCar('tesla', 'x', 2020)

print(new_tesla.get_descriptive_name())
new_tesla.battery.describe_battery()
new_tesla.battery.get_range()

