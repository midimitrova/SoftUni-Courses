def create_seq(n):
    sequence = [0, 1]
    for _ in range(3, n + 1):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


def locate(sequence, number):
    if number in sequence:
        print(f'The number - {number} is at index {sequence.index(number)}')
    else:
        print(f'The number {number} is not in the sequence')