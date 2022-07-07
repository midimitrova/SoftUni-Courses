minutes_kontrol = int(input())
seconds_kontrol = int(input())
distance_metres = float(input())
seconds_100_metres = int(input())

total_kontrol_seconds = (minutes_kontrol * 60) + seconds_kontrol
slower_time = (distance_metres / 120) * 2.5
total_time = (distance_metres / 100) * seconds_100_metres - slower_time

if total_kontrol_seconds >= total_time:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    print(f"No, Marin failed! He was {total_time - total_kontrol_seconds:.3f} second slower.")