rooms = input().split('|')

initial_health = 100
bitcoins = 0
room = 0
current_number = 0
is_killed = False
while True:
    for i in range(len(rooms)):
        current_command, number = rooms[i].split()
        number = int(number)
        room += 1
        if current_command == 'potion':
            current_number = abs(initial_health - 100)
            initial_health += number
            if initial_health > 100:
                initial_health = 100
                print(f"You healed for {current_number} hp.")
            else:
                print(f"You healed for {number} hp.")
            print(f"Current health: {initial_health} hp.")

        elif current_command == 'chest':
            bitcoins += number
            print(f"You found {number} bitcoins.")
        else:
            initial_health -= number
            if initial_health > 0:
                print(f"You slayed {current_command}.")
            else:
                print(f"You died! Killed by {current_command}.")
                print(f"Best room: {room}")
                is_killed = True
                break
    if is_killed:
        break
    if room == len(rooms):
        is_killed = False
        break
if not is_killed:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {initial_health}")
