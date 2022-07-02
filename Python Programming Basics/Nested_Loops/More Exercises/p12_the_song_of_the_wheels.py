control_number = int(input())
cnt = 0
is_have_number = False
number = ""
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                result = a * b + c * d
                if result == control_number and a < b and c > d:
                    cnt += 1
                    if cnt == 4:
                        is_have_number = True
                        number = (f"{a}{b}{c}{d}")
                    print(f"{a}{b}{c}{d}", end=' ')
print()
if is_have_number:
    print(f"Password: {number}")
else:
    print("No!")