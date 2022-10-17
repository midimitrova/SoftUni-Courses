number_of_electrons = int(input())
electrons = []
shell = 1

while number_of_electrons > 0:
    max_electrons_to_fill = 2 * shell ** 2

    if max_electrons_to_fill > number_of_electrons:
        electrons.append(number_of_electrons)
    else:
        electrons.append(max_electrons_to_fill)

    number_of_electrons -= max_electrons_to_fill
    shell += 1

print(electrons)
