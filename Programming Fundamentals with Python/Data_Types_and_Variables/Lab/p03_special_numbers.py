number = int(input())

total_sum = 0

for nums in range(1, number + 1):

    for digit in str(nums):
        total_sum += int(digit)


    if total_sum == 5 or total_sum == 7 or total_sum == 11:
        print(f'{nums} -> True')

    else:
        print(f'{nums} -> False')

    total_sum = 0



