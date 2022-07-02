n = int(input())
l = int(input())


for n1 in range(1, n + 1):
    for n2 in range(1, n + 1):
        for n3 in range(97, 97 + l):
            for n4 in range(97, 97 + l):
                for n5 in range(1, n + 1):
                    if n5 > n1 and n5 > n2:
                        print(f"{n1}{n2}{chr(n3)}{chr(n4)}{n5}", end=" ")
