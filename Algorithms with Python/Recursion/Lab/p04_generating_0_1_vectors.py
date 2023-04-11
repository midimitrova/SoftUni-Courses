def generate(num_idx, vector):
    if num_idx >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[num_idx] = num
        generate(num_idx + 1, vector)


n = int(input())
vector = [0] * n
generate(0, vector)
