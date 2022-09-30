lst_nums = input().split(' ')
cnt_numbers_remove = int(input())

int_lst_nums = []
for num in lst_nums:
    int_lst_nums.append(int(num))

for _ in range(cnt_numbers_remove):
    int_lst_nums.remove(min(int_lst_nums))

print(', '.join(str(element) for element in int_lst_nums))
