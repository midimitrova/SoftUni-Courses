import sys

number = input()

max_number = - sys.maxsize

while number != "Stop":
    current_number = int(number)

    if current_number > max_number:
        max_number = current_number

    number = input()

print(max_number)