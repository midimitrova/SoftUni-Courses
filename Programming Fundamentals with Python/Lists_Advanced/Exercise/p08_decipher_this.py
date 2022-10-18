def character_code(word: str):
    ch_digit = ''
    new_word = []

    for ch in word:
        if ch.isnumeric():
            ch_digit += ch
        else:
            new_word.append(ch)

    ch_at_beginning = chr(int(ch_digit))
    new_word.insert(0, ch_at_beginning)

    return new_word


def decipher_word(word: str):
    new_word = character_code(word)
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    return ''.join(new_word)


message = input().split()
secret_message = [decipher_word(word) for word in message]
print(' '.join(secret_message))
