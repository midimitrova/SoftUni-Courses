number = int(input())

in_range = (-100 <= number <= 100) and number != 0

if not in_range:
    print("No")
else:
    print("Yes")