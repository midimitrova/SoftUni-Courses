number_groups = int(input())


total_people = 0


n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0


for people in range(0, number_groups):
    number_people_in_group = int(input())
    total_people += number_people_in_group
    if number_people_in_group <= 5:

        n1 += number_people_in_group
    elif number_people_in_group <= 12:

        n2 += number_people_in_group

    elif number_people_in_group <= 25:

        n3 += number_people_in_group

    elif number_people_in_group <= 40:

        n4 += number_people_in_group

    else:

        n5 += number_people_in_group



p1 = (n1 / total_people) * 100
p2 = (n2 / total_people) * 100
p3 = (n3 / total_people) * 100
p4 = (n4 / total_people) * 100
p5 = (n5 / total_people) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

