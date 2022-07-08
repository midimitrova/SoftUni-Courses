from math import ceil

high = int(input())
width = int(input())
percentage_not_paint = int(input()) / 100

total_to_paint = high * width * 4
total_paint = total_to_paint - total_to_paint * percentage_not_paint

command = input()

while command != "Tired!":
    paint = int(command)


    total_paint -= paint

    if total_paint <= 0:
        break
    command = input()

if command == "Tired!":
    print(f"{ceil(total_paint)} quadratic m left." )
elif total_paint == 0:
    print("All walls are painted! Great job, Pesho!")
elif total_paint < 0:
    print(f"All walls are painted and you have {abs(ceil(total_paint))} l paint left!")




