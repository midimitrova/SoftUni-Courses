first_seq = input().split(', ')
second_seq = input().split(', ')


substrings = []
for word in first_seq:
    for words in second_seq:
        if word in words and word not in substrings:
            substrings.append(word)
print(substrings)
