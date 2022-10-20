neighborhood = [int(num) for num in input().split("@")]

command = input()
position = 0

while command != 'Love!':
    current_command, index = command.split()
    index = int(index)

    position = position + index

    if position >= len(neighborhood):
        position = 0

    if neighborhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {position}.")

cnt = 0
for num in neighborhood:
    if num != 0:
        cnt += 1

if cnt == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {cnt} places.")
