
num1 = int(input())
num2 = int(input())
num3 = int(input())


max_num = 0

if num1 > num2 and num1 > num3:
    max_num = num1
elif num2 > num1 and num2 > num3:
    max_num = num2
elif num3 > num1 and num3 > num1:
    max_num = num3

print(max_num)