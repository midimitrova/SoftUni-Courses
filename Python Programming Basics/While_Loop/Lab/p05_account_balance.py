total_sum = 0

payment = input()
while payment != "NoMoreMoney":
    current_payment = float(payment)

    if current_payment < 0:
        print("Invalid operation!")
        break

    total_sum += current_payment

    print(f"Increase: {current_payment:.2f}")

    payment = input()

print(f"Total: {total_sum:.2f}")