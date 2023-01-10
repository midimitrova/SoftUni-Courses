text = input()

char_dictionary = {}

for ch in text:
    if ch not in char_dictionary:
        char_dictionary[ch] = 0
    char_dictionary[ch] += 1

for char, count in sorted(char_dictionary.items()):
    print(f'{char}: {count} time/s')