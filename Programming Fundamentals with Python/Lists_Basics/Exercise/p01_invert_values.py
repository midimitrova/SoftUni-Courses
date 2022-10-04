nums = input().split(' ')

int_lst = []

for curr_num in nums:
    int_lst.append(int(curr_num))

reversed_lst = []
for number in int_lst:
    reversed_number = number * -1
    reversed_lst.append(reversed_number)
print(reversed_lst)