import re

number_of_codes = int(input())

digits = ''
pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'

for _ in range(number_of_codes):
    text = input()
    matches = re.match(pattern, text)

    if not matches:
        print('Invalid barcode')
    else:
        numbers = re.findall(r'\d+', matches.group())

        if not numbers:
            print('Product group: 00')
        else:
            print(f'Product group: {"".join(numbers)}')
