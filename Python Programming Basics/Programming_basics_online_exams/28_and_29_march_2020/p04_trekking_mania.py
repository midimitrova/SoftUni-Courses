number_groups = int(input())

people_musala = 0
people_monblan = 0
people_k = 0
people_k2 = 0
people_everest = 0

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for group in range(1, number_groups + 1):
    number_people = int(input())

    if number_people <= 5:
        people_musala += number_people

    elif number_people <= 12:
        people_monblan += number_people
    elif number_people <= 25:
        people_k += number_people
    elif number_people <= 40:
        people_k2 += number_people
    elif number_people >= 41:
        people_everest += number_people

total_people = people_musala + people_monblan + people_k + people_k2 + people_everest

p1 = (people_musala / total_people) * 100
p2 = (people_monblan / total_people) * 100
p3 = (people_k / total_people) * 100
p4 = (people_k2 / total_people) * 100
p5 = (people_everest / total_people) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")