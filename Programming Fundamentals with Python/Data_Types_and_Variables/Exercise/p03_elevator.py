from math import ceil

people = int(input())
capacity = int(input())

people_in_courses = people / capacity
print(ceil(people_in_courses))
