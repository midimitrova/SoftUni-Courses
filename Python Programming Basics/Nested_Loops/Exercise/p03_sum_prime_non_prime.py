from math import ceil

sum_prime = 0
sum_non_prime = 0


command = input()
while command != "stop":
    curr_number = int(command)

    if curr_number < 0:
        print("Number is negative.")
        command = input()
        continue

    if curr_number < 1:
        sum_non_prime += curr_number
    else:

        is_prime = True
        for div in range(2, ceil(curr_number / 2) + 1):
            if curr_number % div == 0:
                is_prime = False
                break

        if is_prime:
            sum_prime += curr_number

        else:
            sum_non_prime += curr_number
    command = input()


print(f"Sum of all prime numbers is: {sum_prime}")

print(f"Sum of all non prime numbers is: {sum_non_prime}")