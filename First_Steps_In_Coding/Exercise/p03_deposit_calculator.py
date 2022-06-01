deposited_amount = int(input())
term_of_deposit = int(input())
annual_interest_rate = float(input())/100
total_sum = deposited_amount + term_of_deposit *((deposited_amount * annual_interest_rate) / 12)
print(total_sum)