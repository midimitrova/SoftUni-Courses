try:
    with open('numbers.txt') as file:
        result = 0
        for line in file:
            result += int(line)
        print(result)
except FileNotFoundError:
    print('No such file')
    