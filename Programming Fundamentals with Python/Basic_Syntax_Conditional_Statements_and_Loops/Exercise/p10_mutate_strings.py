first_string = input()
second_string = input()

transform_list = list(first_string)

for letter in range(len(first_string)):
    if transform_list[letter] != second_string[letter]:
        transform_list[letter] = second_string[letter]
        print("".join(transform_list))