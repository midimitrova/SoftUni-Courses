start_number = int(input())
end_number = int(input())
magic_number = int(input())

combinations_cnt = 0
is_found = False

for a in range(start_number, end_number + 1):
    for b in range(start_number, end_number + 1):
        combinations_cnt += 1
        if a + b == magic_number:
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f"Combination N:{combinations_cnt} ({a} + {b} = {magic_number})")
else:
    print(f"{combinations_cnt} combinations - neither equals {magic_number}")