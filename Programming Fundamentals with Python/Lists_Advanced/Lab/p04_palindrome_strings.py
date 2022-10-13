words = input().split()
palindrome_word = input()

palindrome_list = [word for word in words if word == word[::-1]]
counter_palindrome = palindrome_list.count(palindrome_word)

print(palindrome_list)
print(f'Found palindrome {counter_palindrome} times')
