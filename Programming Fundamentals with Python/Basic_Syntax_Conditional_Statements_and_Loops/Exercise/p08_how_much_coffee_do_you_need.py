

total_coffee = 0

command = input()
while command != 'END':

    if command.lower() not in ['coding', 'dog', 'cat', 'movie']:
        command = input()
        continue

    if command.upper() not in ['CODING', 'DOG', 'CAT', 'MOVIE']:
        command = input()
        continue

    if command.islower():
        total_coffee += 1
    elif command.isupper():
        total_coffee += 2

    command = input()

if total_coffee > 5:
    print("You need extra sleep")
else:
    print(total_coffee)






