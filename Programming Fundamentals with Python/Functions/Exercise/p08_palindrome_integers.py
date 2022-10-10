def palindrome_int(nums):
    for num in nums:
        if num == num[::-1]:
            print('True')
        else:
            print('False')


numbers = input().split(', ')
palindrome_int(numbers)
