budget = float(input())
money_have = float(input())

days = 0
spend_cnt = 0

while money_have < budget and spend_cnt < 5:
    command = input()
    current_money = float(input())
    days += 1

    if command == "save":
        money_have += current_money
        spend_cnt = 0
    elif command == "spend":
        money_have -= current_money
        spend_cnt += 1
        if money_have < 0:
            money_have = 0
if spend_cnt == 5:
    print(f"You can't save the money.")
    print(f"{days}")
if money_have >= budget:
    print(f"You saved the money for {days} days.")