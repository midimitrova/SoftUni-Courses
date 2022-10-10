def loading_bar(num):
    if num < 100:
        return f'{num}% [{"%" * (num//10)}{"." * (10 - (num//10))}]\nStill loading...'
    else:
        return f'{num}% Complete!\n[{(10 * "%")}]'


number = int(input())
print(loading_bar(number))