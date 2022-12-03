population = [int(num) for num in input().split(', ')]
minimum_wealth = int(input())
is_possible = True

for num_index in range(len(population)):
    max_wealth = max(population)
    max_num_index = population.index(max_wealth)
    if population[num_index] < minimum_wealth:
        needed_wealth = minimum_wealth - population[num_index]
        population[num_index] += needed_wealth
        if population[max_num_index] - needed_wealth < minimum_wealth:
            is_possible = False
            print('No equal distribution possible')
            break
        else:
            population[max_num_index] -= needed_wealth

if is_possible:
    print(population)

