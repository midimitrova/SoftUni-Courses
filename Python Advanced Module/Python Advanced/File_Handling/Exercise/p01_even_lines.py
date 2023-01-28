with open('ex1_text.txt') as file:
    even_lines = []
    new_string = []
    # text = file.read().split('\n')
    for row, line in enumerate(file):
        if row % 2 == 0:
            result = ' '.join(reversed(line.strip().split()))
            for char in ["-", ",", ".", "!", "?"]:
                result = result.replace(char, '@')
            print(result)
