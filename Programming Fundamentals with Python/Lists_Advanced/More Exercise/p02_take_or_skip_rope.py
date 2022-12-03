message_to_decrypt = input()

numbers_list = []
letters = ''

for letter_or_digit in message_to_decrypt:
    if letter_or_digit.isdigit():
        numbers_list.append(int(letter_or_digit))
    else:
        letters += letter_or_digit

take_list = []
skip_list = []

for num_index in range(len(numbers_list)):
    if num_index % 2 == 0:
        take_list.append(numbers_list[num_index])
    else:
        skip_list.append(numbers_list[num_index])

final_string = ''

for take, skip in zip(take_list, skip_list):
    if take == 0:
        letters = letters[skip:]
    elif take != 0:
        final_string = final_string + letters[:take]
        letters = letters[skip + take:]

print(final_string)
