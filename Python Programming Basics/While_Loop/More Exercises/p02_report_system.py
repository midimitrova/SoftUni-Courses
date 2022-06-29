charity_sum = int(input())

cash_payment = 0
card_payment = 0
cash_payment_cnt = 0
card_payment_cnt = 0
curr_command_cnt = 0

command = input()
while command != "End":

    curr_command = int(command)

    curr_command_cnt += 1
    if curr_command_cnt % 2 == 0:
        if curr_command < 10:
            print("Error in transaction!")
        else:

            print("Product sold!")
            card_payment_cnt += 1
            card_payment += curr_command
    else:
        if curr_command > 100:
            print("Error in transaction!")

        else:
            print("Product sold!")
            cash_payment_cnt += 1
            cash_payment += curr_command

    if (card_payment + cash_payment) >= charity_sum:
        break

    command = input()

if (card_payment + cash_payment) >= charity_sum:
    print(f"Average CS: {cash_payment / cash_payment_cnt:.2f}")
    print(f"Average CC: {card_payment / card_payment_cnt:.2f}")
else:
    print("Failed to collect required money for charity.")



