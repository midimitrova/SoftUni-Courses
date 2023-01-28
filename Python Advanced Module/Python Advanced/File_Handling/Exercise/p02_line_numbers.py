import string

with open('ex2_text.txt') as file:
    result = []
    text = file.read().split('\n')
    count_alpha = 0
    count_punctuation = 0
    for line in range(len(text)):
        for symbol in text[line]:
            if symbol.isalpha():
                count_alpha += 1
            elif symbol in string.punctuation:
                count_punctuation += 1

        result.append(f'Line {line + 1}: {text[line]} ({count_alpha})({count_punctuation})')
        count_alpha = 0
        count_punctuation = 0

with open('ex2_output.txt', 'a') as file:
    for line in result:
        file.writelines(line + '\n')
