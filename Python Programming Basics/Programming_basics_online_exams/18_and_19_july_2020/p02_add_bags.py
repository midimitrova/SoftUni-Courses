price_more_20_kg = float(input())
kg_luggage = float(input())
days_travelling = int(input())
number_luggage = int(input())

luggage_to_10_kg = price_more_20_kg * 20/100
between_10_20_kg = price_more_20_kg * 50/100



if days_travelling > 30:
    if kg_luggage < 10:
        price = (number_luggage * luggage_to_10_kg) + (number_luggage * luggage_to_10_kg) * 10/100
    elif 10 <= kg_luggage <= 20:
        price = (number_luggage * between_10_20_kg) + (number_luggage * between_10_20_kg) * 10/100
    elif kg_luggage > 20:
        price = (number_luggage * price_more_20_kg) + (number_luggage * price_more_20_kg) * 10/100
elif 7 <= days_travelling <= 30:
    if kg_luggage < 10:
        price = (number_luggage * luggage_to_10_kg) + (number_luggage * luggage_to_10_kg) * 15/100
    elif 10 <= kg_luggage <= 20:
        price = (number_luggage * between_10_20_kg) + (number_luggage * between_10_20_kg) * 15/100
    elif kg_luggage > 20:
        price = (number_luggage * price_more_20_kg) + (number_luggage * price_more_20_kg) * 15/100
elif days_travelling <= 7:
    if kg_luggage < 10:
        price = (number_luggage * luggage_to_10_kg) + (number_luggage * luggage_to_10_kg) * 40/100
    elif 10 <= kg_luggage <= 20:
        price = (number_luggage * between_10_20_kg) + (number_luggage * between_10_20_kg) * 40/100
    elif kg_luggage > 20:
        price = (number_luggage * price_more_20_kg) + (number_luggage * price_more_20_kg) * 40/100
print(f"The total price of bags is: {price:.2f} lv.")