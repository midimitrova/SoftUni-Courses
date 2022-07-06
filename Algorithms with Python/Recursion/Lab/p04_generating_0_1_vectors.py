def my_vector(index, vector):
    if index >= len(vector):
        print(*vector, sep="")
        return
    for num in range(2):
        vector[index] = num
        my_vector(index + 1, vector)


n = int(input())
vector = [None] * n

my_vector(0, vector)