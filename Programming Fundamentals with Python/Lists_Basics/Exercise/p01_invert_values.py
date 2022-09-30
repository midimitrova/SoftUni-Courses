nums = input().split(' ')

int_lst = []

for curr_num in nums:
    int_lst.append(int(curr_num))

reversed_lst = []
for number in int_lst:
    if number > 0:
        number = -abs(number)
        reversed_lst.append(number)
    else:
        number = abs(number)
        reversed_lst.append(number)
print(reversed_lst)