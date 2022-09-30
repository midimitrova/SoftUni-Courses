factor = int(input())
count = int(input())

my_lst = []

for num in range(factor, (factor * count) + 1, factor):
    if num % factor == 0 and num > 0:
        my_lst.append(num)

print(my_lst)
