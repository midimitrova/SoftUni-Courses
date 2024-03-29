def multiply(times):
    def decorator(function):
        def wrapper(num):
            result = function(num)
            return result * times

        return wrapper

    return decorator


# --- test code ---
# @multiply(3)
# def add_ten(number):
#     return number + 10
#
#
# print(add_ten(3))
#
#
# @multiply(5)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(6))

