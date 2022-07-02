last_sector = input()
rows_in_first_sector = int(input())
number_places_in_odd_row = int(input())

sector = ord(last_sector)
cnt = 0
start_sector = 65
start_seat = 97

for sec in range(start_sector, sector + 1):

    for rows in range(1, rows_in_first_sector + 1):
        if rows % 2 != 0:
            for places in range(start_seat, (start_seat + number_places_in_odd_row)):
                print(f"{chr(sec)}{rows}{chr(places)}")

                cnt += 1
                even_places = number_places_in_odd_row + 2
        elif rows % 2 == 0:
            for places in range(start_seat, (start_seat + number_places_in_odd_row + 2)):
                print(f"{chr(sec)}{rows}{chr(places)}")
                cnt += 1
    if rows_in_first_sector + 1 > rows_in_first_sector:
        rows_in_first_sector += 1
print(cnt)



