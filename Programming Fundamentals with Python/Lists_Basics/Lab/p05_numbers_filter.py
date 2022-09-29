n_lines = int(input())

nums_lst = []
command_even = 'even'
command_odd = 'odd'
command_positive = 'positive'
command_negative = 'negative'

for _ in range(n_lines):
    curr_number = int(input())
    nums_lst.append(curr_number)

command = input()

filtered_lst = []
for num in nums_lst:
    if (command == command_even and num % 2 == 0) or \
            (command == command_odd and num % 2 != 0) or \
            (command == command_positive and num >= 0) or \
            (command == command_negative and num < 0):
        filtered_lst.append(num)

print(filtered_lst)
