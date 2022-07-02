start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

combination = 0
is_found = False


for n1 in range(start_interval, end_interval + 1):
    for n2 in range(start_interval, end_interval + 1):
        total_sum = n1 + n2
        combination += 1
        if total_sum == magic_number:
            is_found = True

            break
    if is_found:
        break


if is_found:
   print(f"Combination N:{combination} ({n1} + {n2} = {magic_number})")
else:
   print(f"{combination} combinations - neither equals {magic_number}")
