number_people = int(input())

back_activity = 0
chest_activity = 0
legs_activity = 0
abs_activity = 0
shake = 0
bar = 0
total_activity = 0
total_products = 0

for i in range(1, number_people + 1):
    activity = input()

    if activity == "Back":
        back_activity += 1
        total_activity += 1
    elif activity == "Chest":
        chest_activity += 1
        total_activity += 1
    elif activity == "Legs":
        legs_activity += 1
        total_activity += 1
    elif activity == "Abs":
        abs_activity += 1
        total_activity += 1
    elif activity == "Protein shake":
        shake += 1
        total_products += 1
    elif activity == "Protein bar":
        bar += 1
        total_products += 1

p1 = (total_activity / number_people) * 100
p2 = (total_products / number_people) * 100

print(f"{back_activity} - back")
print(f"{chest_activity} - chest")
print(f"{legs_activity} - legs")
print(f"{abs_activity} - abs")
print(f"{shake} - protein shake")
print(f"{bar} - protein bar")
print(f"{p1:.2f}% - work out")
print(f"{p2:.2f}% - protein")