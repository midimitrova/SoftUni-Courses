age = int(input())

if 0 <= age <= 14:
    print('drink toddy')
elif 15 <= age <= 18:
    print('drink coke')
elif 19 <= age <= 21:
    print('drink beer')
elif age > 21:
    print('drink whisky')