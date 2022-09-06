n = int(input())

while n > 0:

    my_string = input()

    if ',' in my_string or '.' in my_string or '_' in my_string:
        print(f"{my_string} is not pure!")
    else:
        print(f"{my_string} is pure.")

    n -= 1
