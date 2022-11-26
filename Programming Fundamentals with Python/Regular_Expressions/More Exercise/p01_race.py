import re


class Race:

    def __init__(self):
        self.racers = {}
        self.points = 0

    def names(self, names, points: int):
        for name in names:
            self.racers[name] = points

    def get_points(self, text):
        pattern = r'\d'
        matches = re.findall(pattern, text)
        for digit in matches:
            self.points += int(digit)
        return self.points

    def get_names(self, text):
        pattern = r'[A-Za-z]+'
        matches = re.findall(pattern, text)
        joined_name = ''.join(matches)
        if joined_name in self.racers.keys():
            self.racers[joined_name] += race.get_points(text)


names = input().split(', ')

race = Race()
points = 0
race.names(names, points)

while True:

    data = input()

    if data == 'end of race':
        break

    race.get_names(data)
    race.points = 0

sorted_racers = sorted(race.racers.items(), key=lambda item: item[1], reverse=True)

print(f"1st place: {sorted_racers[0][0]}")
print(f"2nd place: {sorted_racers[1][0]}")
print(f"3rd place: {sorted_racers[2][0]}")
