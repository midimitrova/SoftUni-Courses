from .functions import locate, create_seq


def run_fib():
    sequence = []
    while True:
        command = input()

        if command == 'Stop':
            break

        current_command = command.split()

        if current_command[0] == 'Create':
            count = int(current_command[-1])
            sequence = create_seq(count)
            print(*sequence)
        elif current_command[0] == 'Locate':
            number = int(current_command[-1])
            locate(sequence, number)
