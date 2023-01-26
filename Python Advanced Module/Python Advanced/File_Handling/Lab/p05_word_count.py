import re

searched_words = []
with open('words.txt', 'r') as file:
    searched_words = file.read().split()


count_words = {}
with open('input.txt', 'r') as file:
    text = file.read()
    for word in searched_words:
        pattern = fr'\b{word}\b'
        count = len(re.findall(pattern, text, re.IGNORECASE))
        count_words[word] = count

with open('output.txt', 'w') as file:
    sorted_words = sorted(count_words.items(), key=lambda x: -x[1])
    for word, count in sorted_words:
        print(f'{word} - {count}')