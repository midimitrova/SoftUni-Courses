def logged(function):
    def wrapper(*args):
        result = function(*args)
        func_name = function.__name__

        return f'you called {func_name}{args}\nit returned {result}'

    return wrapper


# --- test code ---
# @logged
# def func(*args):
#     return 3 + len(args)
#
# print(func(4, 4, 4))
#
#
# @logged
# def sum_func(a, b):
#     return a + b
#
# print(sum_func(1, 4))
