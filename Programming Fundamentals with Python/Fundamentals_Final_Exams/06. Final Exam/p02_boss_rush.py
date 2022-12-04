import re

number = int(input())

pattern = r'\|(?P<name>[A-Z]{3,})\|\:\#(?P<title>[A-Z][a-z]+\s[A-Z]?[a-z]+)\#'


for _ in range(number):
    message = input()
    matches = re.search(pattern, message)
    if matches:
        data = matches.groupdict()
        print(f'{data["name"]}, The {data["title"]}')
        print(f'>> Strength: {len(data["name"])}')
        print(f'>> Armor: {len(data["title"])}')
    else:
        print('Access denied!')
