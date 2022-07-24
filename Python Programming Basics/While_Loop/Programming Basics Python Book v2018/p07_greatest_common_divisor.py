a = int(input())
b = int(input())

while b != 0:
    curr_b = b
    b = a % b
    a = curr_b
    print("GCD = %d" % a)
