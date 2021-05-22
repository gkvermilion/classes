filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write("i luv my dog. \n")
#     file_object.write("and cat... \n")

with open(filename, 'a') as file_object:
    file_object.write("This is the 3rd string. \n")
    file_object.write("F R A M E D A T A \n")