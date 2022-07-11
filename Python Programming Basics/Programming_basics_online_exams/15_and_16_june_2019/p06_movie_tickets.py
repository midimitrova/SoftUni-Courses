a1 = int(input())
a2 = int(input())
n = int(input())


for n1 in range(a1, a2):
    for n2 in range(1, n):
        for n3 in range(1, int(n / 2)):
            n4 = n1
            result = n2 + n3 + n4
            if n1 % 2 != 0 and result % 2 != 0:
                print(f"{chr(n1)}-{n2}{n3}{ord(chr(n1))}")

