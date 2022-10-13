happiness_list = [int(num) for num in input().split()]
factor = int(input())

happiness = [num * factor for num in happiness_list]

average = sum(happiness) / len(happiness)

happy = [el for el in happiness if el >= average]
sad = [el for el in happiness if el < average]

if len(sad) > len(happiness) / 2:
    print(f'Score: {len(happy)}/{len(happiness)}. Employees are not happy!')
else:
    print(f'Score: {len(happy)}/{len(happiness)}. Employees are happy!')

