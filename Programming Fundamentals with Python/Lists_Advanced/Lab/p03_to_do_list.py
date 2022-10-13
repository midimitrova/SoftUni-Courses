command = input().split('-')
tasks = []

while True:

    if command[0] == 'End':
        break
    importance = int(command[0])
    note = command[1]
    tasks.append((importance, note))

    command = input().split('-')


sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
print(sorted_tasks)