divisor = int(input())
number_range = int(input())

nums = []
max_num = 0

for num in range(1, number_range + 1):

    if num % divisor == 0:
        nums.append(num)

for i in nums:
    if i > max_num:
        max_num = i
print(max_num)




# max_num = nums.pop()
# print(max_num)
