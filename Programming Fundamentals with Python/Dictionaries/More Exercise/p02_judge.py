participants = {'user': {}, 'course': {}}

command = input()
while command != 'no more time':

    name, course, points = command.split(' -> ')
    points = int(points)

    if course not in participants['course']:
        participants['course'][course] = {}

    if name not in participants['course'][course]:
        participants['course'][course][name] = 0

    if name not in participants['user']:
        participants['user'][name] = 0

    if name in participants['user'] and participants['user'][name] == points:
        participants['user'][name] += points

    if participants['course'][course][name] < points:
        participants['user'][name] += points - participants['course'][course][name]
        participants['course'][course][name] = points

    command = input()


def show_result():
    for course in participants['course']:
        print(f"{course}: {len(participants['course'][course])} participants")
        for pos, (name, points) in enumerate(
                sorted(participants['course'][course].items(), key=lambda item: (-item[1], item[0])), 1):
            print(f"{pos}. {name} <::> {points}")
    print("Individual standings:")
    for pos, (name, points) in enumerate(
            sorted(participants['user'].items(), key=lambda item: (-item[1], item[0])), 1):
        print(f"{pos}. {name} -> {points}")


show_result()
