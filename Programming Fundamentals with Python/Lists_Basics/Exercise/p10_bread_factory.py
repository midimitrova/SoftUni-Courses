events = input().split('|')
initial_energy = 100
initial_coins = 100
factory_is_open = True
gained_energy = 0
for event in events:
    event_coin = event.split('-')
    current_event = event_coin[0]
    number = int(event_coin[1])

    if current_event == 'rest':
        current_energy = initial_energy
        initial_energy += number
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif current_event == 'order':
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += number
            print(f'You earned {number} coins.')
        else:
            initial_energy += 50
            print('You had to rest!')
    else:
        if initial_coins >= number:
            initial_coins -= number
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            factory_is_open = False
            break
if factory_is_open:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")

