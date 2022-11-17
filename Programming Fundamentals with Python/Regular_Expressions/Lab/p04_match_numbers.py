import re


class MatchNumber:

    def __init__(self, numbers):
        self.numbers = numbers

    def match(self):
        pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
        searched_numbers = re.finditer(pattern, self.numbers)
        return searched_numbers


number = input()
match_numbers = MatchNumber(number)
matches = match_numbers.match()
valid_numbers = [match.group() for match in matches]
print(*valid_numbers)