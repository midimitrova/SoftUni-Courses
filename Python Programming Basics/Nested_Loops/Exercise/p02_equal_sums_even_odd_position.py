num1 = int(input())
num2 = int(input())

for number in range(num1, num2 + 1):
    number_to_str = str(number)
    even_sum = 0
    odd_sum = 0

    for i, digit in enumerate(number_to_str):
        if i % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=" ")

