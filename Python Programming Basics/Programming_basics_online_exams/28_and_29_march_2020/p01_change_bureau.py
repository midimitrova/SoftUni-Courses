number_bitcoins = int(input())
number_yuna = float(input())
commission = float(input())

bitcoin_in_lv = 1168
yuan_in_lv = 0.15 * 1.76


total_sum_lv = number_bitcoins * bitcoin_in_lv + yuan_in_lv * number_yuna
total_sum_euro = total_sum_lv / 1.95

tax = total_sum_euro * commission/100


final_sum = total_sum_euro - tax


print(f"{final_sum:.2f}")
