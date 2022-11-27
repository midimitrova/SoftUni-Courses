first_chr = input()
second_chr = input()
random_string = input()

start = ord(first_chr)
end = ord(second_chr)

valid_symbols = []
for symbol in random_string:
    if start < ord(symbol) < end:
        valid_symbols.append(ord(symbol))
print(sum(valid_symbols))