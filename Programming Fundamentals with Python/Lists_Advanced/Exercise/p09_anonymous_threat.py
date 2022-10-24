words = input().split()

command = input()
while command != '3:1':

    command = command.split()
    current_command = command[0]

    if current_command == 'merge':
        start = int(command[1])
        end = int(command[2])
        if start < 0:
            start = 0
        if end > len(words) - 1:
            end = len(words) - 1
        for index, string in enumerate(words):
            if index in range(start + 1, end + 1):
                words[start] += words[index]
        for index in range(end, start, - 1):
            words.pop(index)
    elif current_command == 'divide':
        index = int(command[1])
        partitions = int(command[2])

        if partitions > len(words[index]):
            step = 1
        else:
            step = len(words[index]) // partitions
        divide_part = words.pop(index)
        start = 0
        for parts in range(partitions):
            if parts == partitions - 1:
                words.insert(index, divide_part[start::])
                break
            else:
                words.insert(index, divide_part[start: start + step:])
            start += step
            index += 1

    command = input()

print(' '.join(words))
