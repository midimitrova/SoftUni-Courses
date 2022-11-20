import re


destinations = input()

pattern = r'(=|/)([A-Z][a-zA-Z][A-za-z]+)\1'
matches = [el.group(2) for el in re.finditer(pattern, destinations)]
places = ''.join(matches)
travel_points = len(places)
print(f"Destinations: {', '.join(matches)}")
print(f"Travel Points: {travel_points}")