budjet = float(input())
number_gpu = int(input())
number_cpu = int(input())
number_ram = int(input())

price_gpu = number_gpu * 250
price_cpu = price_gpu * 0.35 * number_cpu
price_ram = price_gpu * 0.1 * number_ram

total_price = price_gpu + price_cpu + price_ram

if number_gpu > number_cpu:
    discount = total_price * 0.15
    total_price -= discount

if total_price <= budjet:
    print(f"You have {budjet - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budjet:.2f} leva more!")