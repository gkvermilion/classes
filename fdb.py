from dzzz import *

while True:
    print("\nRegistration")
    print("(enter 'q' at any time to quit)")

    choice = input()
    if choice == 'q':
        break
    else:
        first_name = input('Your name?\n')
        last_name = input('Last name?\n')
        e_mail = input('Your E-Mail address?\n')
        nickname = input('Your nickname?\n')
        password = input('password?\n')
        id_0000 = unique_id(build_profile(first_name,
                                          last_name,
                                          e_mail=e_mail,
                                          nickname=nickname))
        append_file(id_0000)
        quit()