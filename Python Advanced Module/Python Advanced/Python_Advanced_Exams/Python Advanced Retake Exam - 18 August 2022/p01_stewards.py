from collections import deque

seats = input().split(', ')
first_seq = deque([int(x) for x in input().split(', ')])
second_seq = deque([int(x) for x in input().split(', ')])

seat_matches = []
rotations = 0

while len(seat_matches) < 3 and rotations < 10:
    current_first_num = first_seq.popleft()
    current_second_num = second_seq.pop()
    rotations += 1

    result = (current_first_num, current_second_num)
    seat_chr = chr(sum(result))

    seat_one = f'{current_first_num}{seat_chr}'
    seat_two = f'{current_second_num}{seat_chr}'

    if seat_one in seat_matches or seat_two in seat_matches:
        continue
    elif seat_one in seats or seat_two in seats:
        if seat_one in seats:
            seat_matches.append(seat_one)
        else:
            seat_matches.append(seat_two)
    elif seat_one not in seats and seat_two not in seats:
        first_seq.append(current_first_num)
        second_seq.appendleft(current_second_num)

print(f'Seat matches: {", ".join(seat_matches)}')
print(f'Rotations count: {rotations}')
