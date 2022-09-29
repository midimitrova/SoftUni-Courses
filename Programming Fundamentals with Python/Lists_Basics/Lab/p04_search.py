n_lines = int(input())
some_string = input()

command_lst = []
for _ in range(n_lines):
    curr_command = input()
    command_lst.append(curr_command)

filtered_lst = []
for strings in command_lst:
    if some_string in strings:
        filtered_lst.append(strings)

print(command_lst)
print(filtered_lst)