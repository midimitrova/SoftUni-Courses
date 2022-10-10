def characters_long(current_pass):
    if len(current_pass) in range(6, 11):
        return True
    return False


def letters_digits(current_pass):
    if current_pass.isalnum():
        return True
    return False


def count_digits(current_pass):
    cnt = 0
    for digit in current_pass:
        if digit.isdigit():
            cnt += 1
    if cnt >= 2:
        return True
    return False


password = input()
if characters_long(password) and letters_digits(password) and count_digits(password):
    print("Password is valid")
if not characters_long(password):
    print("Password must be between 6 and 10 characters")
if not letters_digits(password):
    print("Password must consist only of letters and digits")
if not count_digits(password):
    print("Password must have at least 2 digits")
