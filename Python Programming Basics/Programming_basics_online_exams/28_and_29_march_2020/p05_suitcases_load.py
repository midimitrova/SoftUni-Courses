capacity = float(input())

luggage_cnt = 0

command = input()
while command != "End":
    luggage_capacity = float(command)

    if luggage_cnt % 3 == 0:
        luggage_capacity += luggage_capacity * 0.01

    if luggage_capacity > capacity:
        break
    luggage_cnt += 1
    capacity -= luggage_capacity
    command = input()
if command == "End":
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {luggage_cnt} suitcases loaded.")
else:
    print("No more space!")
    print(f"Statistic: {luggage_cnt} suitcases loaded.")