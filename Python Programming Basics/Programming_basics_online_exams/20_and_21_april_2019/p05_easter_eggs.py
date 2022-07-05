number_color_eggs = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_color_egg = ""
max_number = 0

for color in range(1, number_color_eggs + 1):
    current_color = input()

    if current_color == "red":
        red_eggs += 1
    elif current_color == "orange":
        orange_eggs += 1
    elif current_color == "blue":
        blue_eggs += 1
    elif current_color == "green":
        green_eggs += 1

if red_eggs > orange_eggs and red_eggs > blue_eggs and red_eggs > green_eggs :
    max_number = red_eggs
    max_color_egg = "red"
elif orange_eggs > red_eggs and orange_eggs > blue_eggs and orange_eggs > green_eggs:
    max_number = orange_eggs
    max_color_egg = "orange"
elif blue_eggs > red_eggs and blue_eggs > orange_eggs and blue_eggs > green_eggs:
    max_number = blue_eggs
    max_color_egg = "blue"
elif green_eggs > red_eggs and green_eggs > orange_eggs and green_eggs > blue_eggs:
    max_number = green_eggs
    max_color_egg = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_number} -> {max_color_egg}")
