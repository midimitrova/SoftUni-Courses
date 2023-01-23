def recursive_power(number, power):
    if power > 0:
        result = number * recursive_power(number, power - 1)
        return result
    else:
        result = 1

    return result


print(recursive_power(2, 3))
print(recursive_power(2, 10))
print(recursive_power(10, 100))
