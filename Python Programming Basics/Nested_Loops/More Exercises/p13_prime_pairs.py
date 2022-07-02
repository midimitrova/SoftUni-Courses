from math import ceil

start_interval_first_numbers = int(input())
start_interval_second_numbers = int(input())
diff_interval_first_numbers = int(input())
diff_interval_second_numbers = int(input())

end_interval_first_numbers = start_interval_first_numbers + diff_interval_first_numbers
end_interval_second_numbers = start_interval_second_numbers + diff_interval_second_numbers


for num1 in range(start_interval_first_numbers, end_interval_first_numbers + 1):
    for num2 in range(start_interval_second_numbers, end_interval_second_numbers + 1):
        is_num1_prime = True
        for div in range(2, ceil(num1 / 2) + 1):
            if num1 % div == 0:
                is_num1_prime = False
                break
        is_num2_prime = True
        for div2 in range(2, ceil(num2 / 2) + 1):
            if num2 % div2 == 0:
                is_num2_prime = False
                break

        if is_num1_prime and is_num2_prime:
            print(f"{num1}{num2}")

