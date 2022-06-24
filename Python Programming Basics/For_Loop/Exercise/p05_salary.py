n_times = int(input())
salary = int(input())


penalty = 0

for name in range(n_times):
    name_website = input()
    
    if name_website == "Facebook":
        penalty = 150

    elif name_website == "Instagram":
        penalty = 100

    elif name_website == "Reddit":
        penalty = 50

    else:
        penalty = 0

    salary -= penalty

    if salary <= 0:
        print(f"You have lost your salary.")
        break

if salary > 0:
    print(salary)