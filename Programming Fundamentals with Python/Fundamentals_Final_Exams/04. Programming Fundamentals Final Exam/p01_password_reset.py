text = input()

password = ''

data = input().split()

while data[0] != 'Done':
    command = data[0]

    if command == 'TakeOdd':
        for chr_index in range(0, len(text)):
            if chr_index % 2 != 0:
                password += text[chr_index]
        text = password
    elif command == 'Cut':
        index = int(data[1])
        lenght = int(data[2])
        string_to_cut = text[index:index+lenght]
        if string_to_cut in text:
            text = text.replace(string_to_cut, '', 1)
    elif command == 'Substitute':
        substring = data[1]
        substitute = data[2]
        if substring in text:
            text = text.replace(substring, substitute)
        else:
            print('Nothing to replace!')
            data = input().split()
            continue

    print(text)

    data = input().split()

print(f'Your password is: {text}')
