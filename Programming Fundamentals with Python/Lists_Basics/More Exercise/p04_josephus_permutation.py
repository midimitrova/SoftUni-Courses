sequence_of_numbers = input().split()
k_number = int(input())
counter = 0
current_index = 0

int_numbers = []
for num in sequence_of_numbers:
    int_numbers.append(int(num))

person_sequence = []

while len(int_numbers) > 0:
    counter += 1

    if counter % k_number == 0:
        person_sequence.append(int_numbers.pop(current_index))
    else:
        current_index += 1

    if current_index >= len(int_numbers):
        current_index = 0

print(str(person_sequence).replace(" ", ""))
