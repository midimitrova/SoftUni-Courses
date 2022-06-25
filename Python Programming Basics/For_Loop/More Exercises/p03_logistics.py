number_cargo = int(input())

price = 0
total_tone = 0
t1 = 0
t2 = 0
t3 = 0


for tone in range(1, number_cargo + 1):
    curr_tone = int(input())

    if curr_tone <= 3:

        price = 200
        t1 += curr_tone
    elif curr_tone <= 11:
         price = 175
         t2 += curr_tone

    elif curr_tone >= 12:
        price = 120
        t3 += curr_tone

total_tone = t1 + t2 + t3
average_price = (t1 * 200 + t2 * 175 + t3 * 120) / total_tone
p1 = (t1 / total_tone) * 100
p2 = (t2 / total_tone) * 100
p3 = (t3 / total_tone) * 100

print(f"{average_price:.2f}")
print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%")
