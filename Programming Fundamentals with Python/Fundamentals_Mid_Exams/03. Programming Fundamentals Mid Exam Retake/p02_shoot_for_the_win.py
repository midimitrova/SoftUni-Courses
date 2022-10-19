numbers = [int(num) for num in input().split()]

shot_cnt = 0
command = input()
while command != 'End':
    shot = int(command)

    for i in range(len(numbers)):
        if shot == i:
            shot_cnt += 1
            current_target = numbers[i]
            numbers[i] = -1
            for i in range(len(numbers)):
                if numbers[i] > current_target and numbers[i] != -1:
                    numbers[i] -= current_target
                elif numbers[i] <= current_target and numbers[i] != -1:
                    numbers[i] += current_target
    command = input()

result = ' '.join(map(str, numbers))
print(f'Shot targets: {shot_cnt} -> {result}')
