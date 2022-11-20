stops = input()

while True:
    data = input().split(':')

    if data[0] == 'Travel':
        print(f'Ready for world tour! Planned stops: {stops}')
        break

    elif data[0] == 'Add Stop':
        index = int(data[1])
        string_to_add = data[2]

        if 0 <= index <= len(stops):
            stops = stops[:index] + string_to_add + stops[index:]

    elif data[0] == 'Remove Stop':
        start_index = int(data[1])
        end_index = int(data[2])
        if 0 <= start_index <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1:]

    elif data[0] == 'Switch':
        old_string = data[1]
        new_string = data[2]

        if old_string in stops:
            stops = stops.replace(old_string, new_string)

    print(stops)
