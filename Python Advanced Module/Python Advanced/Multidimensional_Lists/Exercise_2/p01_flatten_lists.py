line = input().split('|')

sub_lists = []
for sub_list in line[::-1]:
    sub_lists.extend(sub_list.split())
print(*sub_lists)
