start_interval = int(input())
end_interval = int(input())

first_start = int(start_interval / 1000)
second_start = int((start_interval / 100) % 10)
third_start = int((start_interval / 10) % 10)
forth_start = int(start_interval % 10)

first_end = int(end_interval / 1000)
second_end = int((end_interval / 100) % 10)
third_end = int((end_interval / 10) % 10)
forth_end = int(end_interval % 10)

for n1 in range(first_start, first_end + 1):
    for n2 in range(second_start, second_end + 1):
        for n3 in range(third_start, third_end + 1):
            for n4 in range(forth_start, forth_end + 1):

                if n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0 and n4 % 2 != 0:

                    print(f"{n1}{n2}{n3}{n4}", end=" ")