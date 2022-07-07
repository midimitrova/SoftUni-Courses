name = input()

single_points = 0
double_points = 0
triple_points = 0
unsuccessful_shot = 0
successful_shot = 0
total_points = 301
make_points = 0


command = input()

while command != "Retire":

    curr_points = int(input())



    if command == "Single":
        single_points = curr_points
        if single_points > total_points:
            unsuccessful_shot += 1
            command = input()
            continue
        successful_shot += 1
        total_points -= single_points



    elif command == "Double":
        double_points = curr_points * 2
        if double_points > total_points:
            unsuccessful_shot += 1
            command = input()
            continue
        successful_shot += 1
        total_points -= double_points




    elif command == "Triple":
        triple_points = curr_points * 3
        if triple_points > total_points:
            unsuccessful_shot += 1
            command = input()
            continue

        successful_shot += 1
        total_points -= triple_points

    if total_points == 0:

        break

    command = input()

if total_points == 0:
    print(f"{name} won the leg with {successful_shot} shots.")
elif command == "Retire":
    print(f"{name} retired after {unsuccessful_shot} unsuccessful shots.")