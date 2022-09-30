cards = input().split(' ')
number_of_shuffles = int(input())


for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_deck = len(cards) // 2
    left_part = cards[0:middle_of_deck]
    right_part = cards[middle_of_deck::]
    for i in range(len(left_part)):
        final_deck.append(left_part[i])
        final_deck.append(right_part[i])
    cards = final_deck
print(cards)

