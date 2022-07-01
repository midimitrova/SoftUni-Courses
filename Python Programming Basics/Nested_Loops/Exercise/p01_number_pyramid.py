n = int(input())
cnt = 1
is_pyramid_ready = False


for row in range(1, n + 1):
    for cow in range(0, row):

        if cnt > n:
            is_pyramid_ready = True
            break

        print(cnt, end=" ")
        cnt += 1
    if is_pyramid_ready:
        break
    print()