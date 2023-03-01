def is_prime(number):
    if number <= 1:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


def get_primes(numbers):
    for num in numbers:
        if is_prime(num):
            yield num


# --- test code ---
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
#
# print(list(get_primes([-2, 0, 0, 1, 1, 0])))
