class Dog():
    """Simple dog model"""

    def __init__(self, name, age):
        """Initializes attributes name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """Dog sits after command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Dog rolls over after command"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
your_dog = Dog('Kika', 20)

print(f'My dog\'s name is {my_dog.name.title()}.')
print(f'{my_dog.name.title()} is {str(my_dog.age)} years old.')
my_dog.sit()

print(f'\nYour dog\'s name is {your_dog.name.title()}.')
print(f'{your_dog.name.title()} is {str(your_dog.age)} years old.')
your_dog.roll_over()



