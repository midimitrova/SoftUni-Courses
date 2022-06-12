record_in_seconds = float(input())
distance_in_metres = float(input())
time_in_seconds_swim_one_metre = float(input())

time_ivan = distance_in_metres * time_in_seconds_swim_one_metre
slower_time = distance_in_metres // 15
new_time = slower_time * 12.5

total_time = time_ivan + new_time

if total_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_in_seconds:.2f} seconds slower.")