words = input().split()
even_words = [word for word in words if len(word) % 2 == 0]
print('\n'.join(even_words))