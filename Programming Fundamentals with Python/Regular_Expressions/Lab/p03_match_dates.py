import re


class MatchDates:

    def __init__(self, dates):
        self.dates = dates

    def match(self):
        pattern = r'(?P<Day>\d{2})(?P<sep>[-\./])(?P<Month>[A-Z][a-z]{2})(?P=sep)(?P<Year>\d{4})'
        searched_dates = re.finditer(pattern, self.dates)
        return searched_dates


dates = input()
match_dates = MatchDates(dates)
matches = match_dates.match()
for match in matches:
    valid_dates = match.groupdict()
    print(f'Day: {valid_dates["Day"]}, Month: {valid_dates["Month"]}, Year: {valid_dates["Year"]}')
