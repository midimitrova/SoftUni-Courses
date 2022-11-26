import re


class Enigma:

    def __init__(self):
        self.message = []
        self.matches = ''

    def get_msg(self, text):
        letters = ['s', 't', 'a', 'r', 'S', 'T', 'A', 'R']
        count_letters = 0
        self.message = []
        for letter in text:
            if letter in letters:
                count_letters += 1
        for index in range(len(text)):
            self.message.append(chr(ord(text[index]) - count_letters))
        return ''.join(self.message)

    def decrypted(self, text):
        pattern = r'[^@\-\!:>]*?@(?P<name>[A-Z-a-z]+)[^@\-\!:>]*?:(?P<population>\d+)[^@\-\!:>]*?!' \
                  r'(?P<attack>A|D)![^@\-\!:>]*?->(?P<count>\d+)[^@\-\!:>]*?'
        self.matches = re.match(pattern, text)
        return self.matches


number = int(input())
enigma = Enigma()
new_msg = []

for _ in range(number):
    data = input()
    new_msg.append(enigma.get_msg(data))
count_a = 0
count_d = 0
planets = {'A': [], 'D': []}

for decrypted_msg in new_msg:
    if enigma.decrypted(decrypted_msg):
        result = enigma.decrypted(decrypted_msg).groupdict()
        if result['attack'] == 'A':
            count_a += 1
            planets['A'].append(result['name'])

        else:
            count_d += 1
            planets['D'].append(result['name'])

print(f"Attacked planets: {count_a}")
sorted_planets = sorted(planets['A'])
[print(f"-> {planet}") for planet in sorted_planets]
print(f"Destroyed planets: {count_d}")
sorted_planets = sorted(planets['D'])
[print(f"-> {planet}") for planet in sorted_planets]
