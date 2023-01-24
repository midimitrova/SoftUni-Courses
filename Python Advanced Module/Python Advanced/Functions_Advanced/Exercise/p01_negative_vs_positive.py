numbers = [int(x) for x in input().split()]

positive = sum([x for x in numbers if x > 0])
negative = sum([x for x in numbers if x < 0])

print(negative)
print(positive)

if abs(negative) > positive:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')



