import json

username = input("What's your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We will remember you when you will comeback, "
          + username + "!")
    