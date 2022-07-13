from math import ceil


end_interval_first_num = int(input())
end_interval_second_num = int(input())
end_interval_third_num = int(input())




for n1 in range(1, end_interval_first_num + 1):
    for n2 in range(2, end_interval_second_num + 1):
        for n3 in range(1, end_interval_third_num + 1):
            is_prime = True
            for div in range(2, ceil(n2 / 2) + 1):
                if n2 % div == 0:
                    is_prime = False
                    break
            if n1 % 2 == 0 and n3 % 2 == 0 and is_prime == True:
                print(f"{n1} {n2} {n3}")