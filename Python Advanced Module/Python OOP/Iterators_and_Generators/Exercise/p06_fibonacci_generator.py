def fibonacci():
    fib0 = 0
    fib1 = 1

    yield fib0
    yield fib1

    while True:
        result = fib0 + fib1
        fib0 = fib1
        fib1 = result

        yield result


# --- test code ---
# generator = fibonacci()
# for i in range(5):
#     print(next(generator))
#
# generator = fibonacci()
# for i in range(1):
#     print(next(generator))

