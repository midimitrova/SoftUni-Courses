num_lst = input().split(', ')

temp = []
zeros = []

for number in num_lst:
    if int(number) != 0:
        temp.append(int(number))
    else:
        zeros.append(int(number))

print(temp + zeros)
