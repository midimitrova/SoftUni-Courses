def odd_and_even_sum(num):
    odd_sum = 0
    even_sum = 0
    for digit in num:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return odd_sum, even_sum


number = input()
odd, even = odd_and_even_sum(number)
print(f"Odd sum = {odd}, Even sum = {even}")