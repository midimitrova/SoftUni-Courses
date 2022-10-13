vowels = ['a', 'o', 'u', 'e', 'i']
word = input()

print(''.join([el for el in word if el.lower() not in vowels]))
