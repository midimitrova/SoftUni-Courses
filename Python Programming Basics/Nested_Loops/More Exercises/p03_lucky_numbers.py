n = int(input())

# first_sum = 0
# second_sum = 0

for n1 in range(1, 10):
    for n2 in range(1, 10):
        for n3 in range(1, 10):
            for n4 in range(1, 10):
                first_sum = n1 + n2
                second_sum = n3 + n4
                if first_sum == second_sum and n % first_sum == 0:
                    print(f"{n1}{n2}{n3}{n4}", end=" ")
