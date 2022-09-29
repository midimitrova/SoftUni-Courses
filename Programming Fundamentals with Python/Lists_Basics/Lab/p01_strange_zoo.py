command_lst = []

for _ in range(3):
    command = input()
    command_lst.append(command)

command_lst[0], command_lst[2] = command_lst[2], command_lst[0]
print(command_lst)