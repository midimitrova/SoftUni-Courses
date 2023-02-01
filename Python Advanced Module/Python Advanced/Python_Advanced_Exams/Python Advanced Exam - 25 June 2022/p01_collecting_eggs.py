from collections import deque

egg_size = deque([int(x) for x in input().split(', ')])
paper_size = deque([int(x) for x in input().split(', ')])

box_size = 50
filled_boxes = 0

while egg_size and paper_size:
    current_egg = egg_size.popleft()
    current_paper = paper_size.pop()

    if current_egg <= 0:
        paper_size.append(current_paper)
        continue

    if current_egg == 13:
        first_paper = paper_size.popleft()
        paper_size.appendleft(current_paper)
        paper_size.append(first_paper)
        continue

    sum_egg_paper = current_paper + current_egg

    if sum_egg_paper <= box_size:
        filled_boxes += 1
    else:
        continue

if filled_boxes > 0:
    print(f'Great! You filled {filled_boxes} boxes.')
else:
    print('Sorry! You couldn\'t fill any boxes!')

if egg_size:
    print(f'Eggs left: {", ".join(map(str, egg_size))}')

if paper_size:
    print(f'Pieces of paper left: {", ".join(map(str, paper_size))}')
