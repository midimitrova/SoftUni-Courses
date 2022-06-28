free_space_width = int(input())
free_space_lenght = int(input())
free_space_high = int(input())

left_space = free_space_width * free_space_lenght * free_space_high

command = input()
while command != "Done":
    number_box = int(command)

    left_space -= number_box

    if left_space < 0:
        break

    command = input()

if command == "Done":
    print(f"{left_space} Cubic meters left.")
elif left_space < 0:
    print(f"No more free space! You need {abs(left_space)} Cubic meters more.")
