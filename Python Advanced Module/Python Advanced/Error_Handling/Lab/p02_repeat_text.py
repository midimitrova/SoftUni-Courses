text = input()

result = ''

try:
    n_times_to_repeat = int(input())
    result = text * n_times_to_repeat
except ValueError:
    print("Variable times must be an integer")

print(result)
