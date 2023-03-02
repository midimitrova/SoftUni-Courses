def cache(function):
    log = {}

    def wrapper(num):
        if num in log:
            return log[num]

        result = function(num)
        log[num] = result

        return result

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# --- test code ---
# fibonacci(3)
# print(fibonacci.log)
#
# fibonacci(4)
# print(fibonacci.log)

