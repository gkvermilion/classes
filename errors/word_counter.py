import os.path

def count_words(filename):
    '''Подсчет количества слов в файле'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " doesn't exist."
        # print(msg)
        pass
    else:
#         Подсчет приблизительного количества строк в файле
        words = contents.split()
        num_words = len(words)
        print("The file " + os.path.basename(filename) + " has about " +
              str(num_words) + " words.")

filepath = '/Users/kali/PycharmProjects/classes/text_files/alice.txt'
count_words(filepath)


filenames = [
    filepath,
    filepath,
    'pi_digits.txt',
    '/Users/kali/PycharmProjects/classes/text_files/pi_million_digits.txt',
    'lines.txt'
]

for file in filenames:
    count_words(file)
