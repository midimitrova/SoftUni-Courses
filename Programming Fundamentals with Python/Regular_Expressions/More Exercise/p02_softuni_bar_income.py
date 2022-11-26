import re


class Bar:

    def __init__(self):
        self.matches = ''

    def get_items(self, text):
        pattern = r'%(?P<name>[A-Z][a-z]+)%[^%\|\.\$]*<(?P<product>\w+)>[^%\|\.\$]*\|(?P<quantity>\d+)' \
                  r'\|[^%\|\.\$]*?(?P<price>\d+(\.(\d+))?)\$'
        self.matches = re.match(pattern, text)
        return self.matches


data = input()
bar = Bar()
total_income = 0
while data != 'end of shift':
    if bar.get_items(data):
        result = bar.get_items(data).groupdict()
        total_income += int(result['quantity']) * float(result['price'])
        print((f"{result['name']}: {result['product']} - {int(result['quantity']) * float(result['price']):.2f}"))

    data = input()

print(f"Total income: {total_income:.2f}")
