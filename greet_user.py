import json

filename = 'username.json'

# with open(filename) as f_obj:
#     username = json.load(f_obj)
#     print("Welcome back, " + username + "!")

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What's your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We will remember you when you come back, "
              + username + "!")
else:
    print("Welcome back, " + username + "!")
    