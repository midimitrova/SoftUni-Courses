class Parking:

    def __init__(self):
        self.users = {}

    def register(self, username: str, plate_number: str):
        if username in self.users.keys():
            print(f"ERROR: already registered with plate number {self.users[username]}")
        else:
            self.users[username] = plate_number
            print(f"{username} registered {self.users[username]} successfully")

    def unregister(self, username: str):
        if username not in self.users.keys():
            print(f"ERROR: user {username} not found")
        else:
            del self.users[username]
            print(f"{username} unregistered successfully")


parking = Parking()
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    data = command[0]
    username = command[1]
    if data == 'register':
        plate = command[2]
        parking.register(username, plate)
    elif data == 'unregister':
        parking.unregister(username)

for name, plate_number in parking.users.items():
    print(f"{name} => {parking.users[name]}")
