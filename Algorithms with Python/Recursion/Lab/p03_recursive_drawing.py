def my_figure(n):
    if n == 0:
        return
    print('*' * n)
    my_figure(n - 1)
    print('#' * n)

n = int(input())

my_figure(n)