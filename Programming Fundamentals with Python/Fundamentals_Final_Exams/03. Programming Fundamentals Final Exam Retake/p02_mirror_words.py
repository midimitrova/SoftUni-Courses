import re

text = input()
pattern = r'(@|#)(?P<word1>[a-zA-Z]{3,})\1\1(?P<word2>[A-Za-z]{3,})\1'
words = [el.groupdict() for el in re.finditer(pattern, text)]

if not words:
    print('No word pairs found!')
    print('No mirror words!')
else:
    print(f'{len(words)} word pairs found!')
    mirror_words = []
    for el in words:
        if el['word1'] == el['word2'][::-1]:
            mirror_words.append(f"{el['word1']} <=> {el['word2']}")
    if not mirror_words:
        print("No mirror words!")
    else:
        print('The mirror words are:')
        print(*mirror_words, sep=", ")