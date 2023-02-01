def forecast(*args):
    sunny_sorted = []
    for data in args:
        if 'Sunny' in data:
            sunny_sorted.append(data)
    sort_sunny = sorted(dict(sunny_sorted).items(), key=lambda x: x[0])
    rainy_sorted = []
    for data in args:
        if 'Rainy' in data:
            rainy_sorted.append(data)
    sort_rainy = sorted(dict(rainy_sorted).items(), key=lambda x: x[0])
    cloudy_sorted = []
    for data in args:
        if 'Cloudy' in data:
            cloudy_sorted.append(data)
    sort_cloudy = sorted(dict(cloudy_sorted).items(), key=lambda x: x[0])

    end_result = []
    end_result.extend(sort_sunny)
    end_result.extend(sort_cloudy)
    end_result.extend(sort_rainy)

    result = ''
    for city, weather in end_result:
        result += f'{city} - {weather}\n'

    return result

# --- TEST CODE ---
# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))
#
# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))
#
# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))
