number = int(input())

for _ in range(number):
    data = input()
    collected_names = []
    collected_age = []
    for letter_index in range(len(data)):
        if data[letter_index] == '@':
            while data[letter_index] != '|':
                letter_index += 1
                if data[letter_index] == '|':
                    break
                collected_names.append(data[letter_index])
    for digit_index in range(len(data)):
        if data[digit_index] == '#':
            while data[digit_index] != '*':
                digit_index += 1
                if data[digit_index] == '*':
                    break
                collected_age.append(data[digit_index])

    print(f"{''.join(collected_names)} is {''.join(collected_age)} years old.")
