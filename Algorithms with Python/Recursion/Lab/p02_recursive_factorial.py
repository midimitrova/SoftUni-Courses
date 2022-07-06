def my_factorial(n):
    if n < 1:
        return 1
    return n * my_factorial(n - 1)


n = int(input())


print(my_factorial(n))