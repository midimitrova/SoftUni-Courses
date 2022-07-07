wanted_high = int(input())

first_jump = wanted_high - 30

tries_cnt = 0
tries_no_cnt = 0

while tries_no_cnt != 3 and first_jump <= wanted_high:
    jump_high = int(input())

    if jump_high > first_jump:
        first_jump += 5
        tries_no_cnt = 0

    else:
        tries_no_cnt += 1

    tries_cnt += 1

if first_jump <= wanted_high:
    print(f"Tihomir failed at {first_jump}cm after {tries_cnt} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {wanted_high}cm after {tries_cnt} jumps.")



