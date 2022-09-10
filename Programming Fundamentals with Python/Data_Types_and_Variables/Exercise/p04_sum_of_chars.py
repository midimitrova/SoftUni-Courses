n = int(input())


total_sum = 0

if n in range(1, 21):
    while n > 0:
        char = input()

        sum = ord(char)
        total_sum += sum


        n -= 1

print(f"The sum equals: {total_sum}")