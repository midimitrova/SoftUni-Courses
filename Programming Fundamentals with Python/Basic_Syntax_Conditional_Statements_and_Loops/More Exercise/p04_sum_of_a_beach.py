my_string = input().lower()

cnt = 0
my_list = ["sand", "water", "fish", "sun"]

for item in my_list:
    if item in my_string:
        word_found = my_string.count(item)
        cnt += word_found

print(cnt)
