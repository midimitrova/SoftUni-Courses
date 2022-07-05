number_eggs = int(input())

# left_eggs = 0
command = input()
sold_eggs = 0

while command != "Close":

    eggs = int(input())

    if command == "Fill":
        # left_eggs = number_eggs + eggs
        number_eggs += eggs

    if number_eggs < eggs:
        break

    if command == "Buy":
        # left_eggs = number_eggs - eggs
        sold_eggs += eggs
        number_eggs -= eggs

    command = input()

if command == "Close":
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")
else:
    print("Not enough eggs in store!")
    print(f"You can buy only {number_eggs}.")