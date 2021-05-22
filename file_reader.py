with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# относительный путь
with open('text_files/pi_digits_2.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
# для мак ос / для windows \

# абсолютный путь
file_path = '/Users/kali/Documents/document.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
#############################################

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
#############################################

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
#############################################
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
print(lines)

#############################################

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

###############################################

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

###############################################

filename = 'text_files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:52] + "...")
print(len(pi_string))

#################################################

filename = 'text_files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Введите свою дату рождения в формате ДД/ММ/ГГ: ")
if birthday in pi_string:
    print("Ваш ДР есть в числе ПИ")
else:
    print("Вашего ДР нет в числе ПИ")
