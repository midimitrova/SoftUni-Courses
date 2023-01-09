from collections import deque


def convert_str_to_seconds(str_time):
    hour, minutes, seconds = [int(x) for x in str_time.split(':')]
    return hour * 60 * 60 + minutes * 60 + seconds


def convert_seconds_to_str_time(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots = input().split(';')
robots_data = {}
busy_time_by_robot = {}

for robot in robots:
    name, time = robot.split('-')
    time = int(time)
    robots_data[name] = time
    busy_time_by_robot[name] = -1

time = convert_str_to_seconds(input())

products = deque()
product = input()
while product != 'End':
    products.append(product)
    product = input()

while products:
    time += 1
    item = products.popleft()
    for name, busy_until in busy_time_by_robot.items():
        if time >= busy_until:
            busy_time_by_robot[name] = time + robots_data[name]
            print(f'{name} - {item} [{convert_seconds_to_str_time(time)}]')
            break
    else:
        products.append(item)
