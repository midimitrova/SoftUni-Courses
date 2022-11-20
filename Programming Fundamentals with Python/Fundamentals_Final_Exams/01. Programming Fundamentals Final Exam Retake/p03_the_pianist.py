number = int(input())

pieces = {}

for _ in range(number):
    data_pieces = input().split('|')
    piece_to_add = data_pieces[0]
    pieces[piece_to_add] = {data_pieces[1]: data_pieces[2]}

while True:
    data = input()

    if data == 'Stop':
        break

    data = data.split('|')
    command = data[0]

    if command == 'Add':
        piece = data[1]
        composer = data[2]
        key = data[3]
        if piece not in pieces.keys():
            pieces[piece] = {composer: key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command == 'Remove':
        piece = data[1]
        if piece in pieces.keys():
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == 'ChangeKey':
        piece = data[1]
        new_key = data[2]
        if piece in pieces.keys():
            value = pieces[piece]
            composer = ''
            for k in value.keys():
                composer = k
            pieces[piece][composer] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
            continue
        print(f'Invalid operation! {piece} does not exist in the collection.')

for piece, value in pieces.items():
    current_value = value.keys()
    for k in current_value:
        composer = k
        key = pieces[piece][composer]
        print(f'{piece} -> Composer: {composer}, Key: {key}')
