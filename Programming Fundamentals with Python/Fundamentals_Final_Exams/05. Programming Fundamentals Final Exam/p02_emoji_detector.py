import re

threshold = 1
coolness = {}
current_coolness = 0
cool_one = {}

text = input()
pattern_emojis = r'([\:]{2}|[\*]{2})([A-Z][a-z]{2,})(\1)'
valid_emojis = re.findall(pattern_emojis, text)

pattern_digits = r'\d'
valid_digits = re.findall(pattern_digits, text)

for digit in valid_digits:
    threshold *= int(digit)

for emoji in valid_emojis:
    for letter in emoji[1]:
        current_coolness += ord(letter)

    coolness[emoji] = current_coolness
    current_coolness = 0

for emoji, value in coolness.items():
    if value > threshold:
        cool_one[emoji] = value

print(f'Cool threshold: {threshold}')
if valid_emojis:
    print(f'{len(coolness)} emojis found in the text. The cool ones are:')
    if cool_one:
        for emoji in cool_one.keys():
            print(''.join(emoji))
