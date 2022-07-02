number_man = int(input())
number_woman = int(input())
max_tables = int(input())

cnt = 0

for client1 in range(1, number_man + 1):
    for client2 in range(1, number_woman + 1):
        cnt += 1
        if cnt > max_tables:
            break
        print(f"({client1} <-> {client2})", end=" ")