while True:
    number = float(input())
    if number < 0:
        print(f"Negative number!")
        break
    else:
        result = number * 2
        print(f"Result: {result:.2f}")