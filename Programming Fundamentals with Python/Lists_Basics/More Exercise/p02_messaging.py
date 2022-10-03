number_sequence = input().split()
text = input()

my_message = []

for number in number_sequence:
    a = len(text)
    sum_digits = 0
    for digit in number:
        sum_digits += int(digit)

    sum_digits %= len(text)


    my_message.append(text[sum_digits])
    text = text.replace(text[sum_digits],'',1)
print(''.join(my_message))
