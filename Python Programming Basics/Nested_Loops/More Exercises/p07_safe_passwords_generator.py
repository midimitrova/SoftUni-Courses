a = int(input())
b = int(input())
generated_pass = int(input())
cnt_pass = 0
is_right = False
for sym1 in range(35, 55):
    for sym2 in range(64, 96):
        for sym3 in range(1, a + 1):
            for sym4 in range(1, b + 1):
                cnt_pass += 1

                if cnt_pass > generated_pass:
                    is_right = True
                    break
                print(f"{chr(sym1)}{chr(sym2)}{sym3}{sym4}{chr(sym2)}{chr(sym1)}", end="|")

                if sym3 == a and sym4 == b:
                    is_right = True
                    break
                sym1 += 1
                if sym1 > 55:
                    sym1 = 35
                sym2 += 1
                if sym2 > 96:
                    sym2 = 64

                if is_right:
                    break

            if is_right:
                break

        if is_right:
            break
    if is_right:
        break



