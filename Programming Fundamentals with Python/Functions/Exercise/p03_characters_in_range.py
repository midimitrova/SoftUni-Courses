def characters(first_chr, end_chr):
    char_list = []
    for symbol in range(ord(first_chr) + 1, ord(end_chr)):
        char_list.append(chr(symbol))
    return char_list


start = input()
end = input()
result = ' '.join(characters(start,end))
print(result)