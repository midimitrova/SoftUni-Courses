start_interval = input()
end_interval = input()
miss_char = input()
cnt = 0
ch1 = ord(start_interval)
ch2 = ord(end_interval)
ch3 = ord(miss_char)

for x in range(ch1, ch2 + 1):
    for y in range(ch1, ch2 + 1):
        for z in range(ch1, ch2 + 1):
            if z == ch3 or y == ch3 or x == ch3:
                continue
            cnt += 1
            print(f"{chr(x)}{chr(y)}{chr(z)}", end=" ")
print(cnt)



