gifts = input().split(' ')

command = input()
while command != 'No Money':
    command = command.split(' ')
    if command[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = 'None'
    elif command[0] == "Required":
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = command[1]
    elif command[0] == "JustInCase":
        gifts[-1] = command[1]
    command = input()

for gift in gifts:
    if gift != 'None':
        print(gift, end=' ')
