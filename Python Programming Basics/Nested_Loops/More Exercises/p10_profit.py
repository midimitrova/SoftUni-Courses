number_of_one = int(input())
number_of_two = int(input())
number_of_five = int(input())
total_sum = int(input())


for n1 in range(0, number_of_one + 1):
    for n2 in range(0, number_of_two + 1):
        for n3 in range(0, number_of_five + 1):

            if total_sum == n1 * 1 + n2 * 2 + n3 * 5:
                print(f"{n1} * 1 lv. + {n2} * 2 lv. + {n3} * 5 lv. = {total_sum} lv.")
