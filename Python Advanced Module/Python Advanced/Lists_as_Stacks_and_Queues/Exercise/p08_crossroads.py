from collections import deque

green_light_seconds = int(input())
free_window_seconds = int(input())
crash = False
total_cars_passed = 0
crash_result = ""
cars = deque()

while True:
    command = input()
    if command == "END" or crash:
        break
    if command != "green":
        cars.append(command)
    else:
        green_light_seconds_left = green_light_seconds
        while cars and green_light_seconds_left > 0:
            car = cars.popleft()
            if len(car) <= green_light_seconds_left:
                green_light_seconds_left -= len(car)
                total_cars_passed += 1
            elif len(car) <= green_light_seconds_left + free_window_seconds:
                free_window_seconds -= len(car) + green_light_seconds_left
                green_light_seconds_left = 0
                total_cars_passed += 1
            else:
                crash = True
                characters_passed = green_light_seconds_left + free_window_seconds
                character_hit = car[characters_passed:characters_passed + 1]
                crash_result = f"{car} was hit at {character_hit}."
                break

if not crash:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")
else:
    print("A crash happened!")
    print(f"{crash_result}")
