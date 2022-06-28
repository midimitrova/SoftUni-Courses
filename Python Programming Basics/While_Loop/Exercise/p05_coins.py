from math import floor

coins = 0
change = float(input())
change_st = change * 100

while change_st > 0:

    if change_st >= 200:
        change_st -= 200
        coins += 1
    elif 200 > change_st >= 100:
        change_st -= 100
        coins += 1
    elif 100 > change_st >= 50:
        change_st -= 50
        coins += 1
    elif 50 > change_st >= 20:
        change_st -= 20
        coins += 1
    elif 20 > change_st >= 10:
        change_st -= 10
        coins += 1
    elif 10 > change_st >= 5:
        change_st -= 5
        coins += 1
    elif 5 > change_st >= 2:
        change_st -= 2
        coins += 1
    elif 2 > change_st >= 1:
        change_st -= 1
        coins += 1
    change_st = floor(change_st)
print(coins)