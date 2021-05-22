# print(5/0)
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

print("Division Calc")
print("Enter q to quit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("Second number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("arguments must be a number!")
    else:
        print(answer)

