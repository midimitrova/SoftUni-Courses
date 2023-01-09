from collections import deque

price_of_bullet = int(input())
size_of_the_gun_barrel = int(input())
bullets_stack = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
value_of_the_intelligence = int(input())

bullets_count = 0
current_len_of_bullets = len(bullets_stack)

while True:
    if bullets_count >= size_of_the_gun_barrel and bullets_stack:
        print('Reloading!')
        bullets_count = 0

    if len(bullets_stack) == 0 or len(locks) == 0:
        break

    current_bullet = bullets_stack[-1]
    current_lock = locks[0]

    if current_lock >= current_bullet:
        print('Bang!')
        bullets_stack.pop()
        locks.popleft()
    else:
        print('Ping!')
        bullets_stack.pop()

    bullets_count += 1

used_bullets = current_len_of_bullets - len(bullets_stack)

if len(locks) == 0:
    print(f'{len(bullets_stack)} bullets left. Earned ${value_of_the_intelligence - (used_bullets * price_of_bullet)}')
else:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')
