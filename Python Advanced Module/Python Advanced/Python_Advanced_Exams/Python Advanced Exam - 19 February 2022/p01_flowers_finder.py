from collections import deque

words_dictionary = {
    'rose': 'rose',
    'tulip': 'tulip',
    'lotus': 'lotus',
    'daffodil': 'daffodil',
}


vowels_deque = deque(input().split())
consonants_stack = input().split()

is_found = False
while vowels_deque and consonants_stack:

    current_vowel = vowels_deque.popleft()
    current_consonant = consonants_stack.pop()

    for word, value in words_dictionary.items():
        if current_vowel in word:
            words_dictionary[word] = words_dictionary[word].replace(current_vowel, '')
        if current_consonant in word:
            words_dictionary[word] = words_dictionary[word].replace(current_consonant, '')

    for word, value in words_dictionary.items():
        if value == '':
            print(f'Word found: {word}')
            is_found = True
            break

    if is_found:
        break

if not is_found:
    print('Cannot find any word!')
if vowels_deque:
    print(f'Vowels left: {" ".join(map(str, vowels_deque))}')
if consonants_stack:
    print(f'Consonants left: {" ".join(map(str, consonants_stack))}')