import re


class MatchPhoneNumber:

    def __init__(self, numbers):
        self.numbers = numbers

    def match(self):
        pattern = r'(\+359)([- ])(2)\2(\d{3})\2(\d{4})\b'
        searched_phones = re.finditer(pattern, self.numbers)
        return searched_phones


phones = input()
match_phones = MatchPhoneNumber(phones)
matches = match_phones.match()
valid_phones = [match.group() for match in matches]
print(', '.join(valid_phones))
