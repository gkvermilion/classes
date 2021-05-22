import os.path

filepath = '/Users/kali/PycharmProjects/classes/text_files/alice.txt'
filename = filepath.split(sep='/')
filename = filename[-1]

try:
    with open(filepath) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " doesn't exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " +
          str(num_words) + " words.")

print(os.path.abspath(filepath))
print(os.path.basename(filepath))
