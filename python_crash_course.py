# A little crash course -- comments begin with a "#"

print('Hello, World! My name is Jen.')


my_var = 'Jen Lu'


4 + 5


for i in range(5):
    print(i * 2)


if my_var == 'Jen Lu':
    print('Horray!')
else:
    print('Boo Hoo')


def square(num):
    return num * num
print(square(4)) # This gives you 16
                 # A longer comment...


class Animal:
    """
    Classes bind data (e.g. name, sound) to behavior (e.g. crying).
    """

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def cry(self):
        print('I make a {} making a {}'.format(self.name, self.sound))

cub = Animal('Lion', 'Roar')
cub.cry()


# Lists (Array)
family = ['Jen Lu', 'John Tran', 'Kim Prosser']
family.append('Simon Lee') # Our family just got bigger
print(family)

# Dictionaries
ages = {
    'Jen': 27,
    'Simon': 27,
    'John': 30,
    'Frank': 99,
}
print('How old is Frank? {}'.format(ages['Frank']))

# Lots of libraries
import math
print(math.pi)
print(math.factorial(7)) # 5040

import django
django.get_version()

quit() # Goodbye