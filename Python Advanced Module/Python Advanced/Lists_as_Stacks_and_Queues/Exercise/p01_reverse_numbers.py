numbers_to_reverse = input().split()

while numbers_to_reverse:
    popped_item = numbers_to_reverse.pop()
    print(popped_item, end=' ')
