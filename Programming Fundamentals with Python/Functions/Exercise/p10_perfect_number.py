def perfect_number(num):
    sum_digits = 0
    for divisor in range(1, (num // 2) + 1):
        if num % divisor == 0:
            sum_digits += divisor

    if sum_digits == num:
        return True
    return False


number = int(input())
if perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
