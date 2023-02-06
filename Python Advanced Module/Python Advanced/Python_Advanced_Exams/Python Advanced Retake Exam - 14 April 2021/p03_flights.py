def flights(*args):
    flights_data = {}

    idx = 0

    while True:
        command = args[idx]
        if ' ' in command:
            command = command.replace(' ', '')
        if args[idx] == 'Finish':
            break
        elif command.isalpha():
            if args[idx] not in flights_data.keys():
                flights_data[args[idx]] = args[idx+1]
            else:
                flights_data[args[idx]] += args[idx+1]
        idx += 2

    return flights_data


# --- TEST CODE ---
# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
#
# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
#
# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
