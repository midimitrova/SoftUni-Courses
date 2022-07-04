from math import ceil, floor

record_seconds = float(input())
distance_metres = float(input())
seconds_for_metre = float(input())

time_total = distance_metres * seconds_for_metre
total = floor(distance_metres / 50)
time = total * 30
final_time = (time + time_total)

if record_seconds > final_time:
    print(f"Yes! The new record is {final_time:.2f} seconds.")
else:
    print(f"No! He was {final_time - record_seconds:.2f} seconds slower.")
