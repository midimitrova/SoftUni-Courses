my_string = input()

capital_letters = []

for i in range(len(my_string)):

    if my_string[i].isupper():
        capital_letters.append(i)

print(capital_letters)