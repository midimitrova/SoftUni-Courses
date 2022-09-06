n = int(input())

are_even = False

while n != 0:
    num = int(input())

    if num % 2 != 0:
        print(f"{num} is odd!")
        are_even = False
        break
    else:
        are_even = True
    n -= 1

if are_even == True:
    print("All numbers are even.")