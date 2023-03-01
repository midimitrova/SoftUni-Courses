def reverse_text(string):
    chr_index = len(string) - 1

    while chr_index >= 0:
        yield string[chr_index]

        chr_index -= 1


for char in reverse_text("step"):
    print(char, end='')
