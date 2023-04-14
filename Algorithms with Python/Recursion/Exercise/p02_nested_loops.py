def recursion_nested_loops(num_idx, vector):
    if num_idx >= len(vector):
        print(*vector, sep=' ')
        return
    for num in range(1, n + 1):
        vector[num_idx] = num
        recursion_nested_loops(num_idx + 1, vector)


n = int(input())
vector = [None] * n
recursion_nested_loops(0, vector)
