import re


class Numbers:

    def __init__(self, text):
        self.text = text
        self.valid = []

    def get_numbers(self):
        pattern = r'\d+'
        while self.text != '':
            valid_numbers = [el for el in re.findall(pattern, self.text)]
            self.valid.extend(valid_numbers)
            self.text = input()

        return self.valid


data = input()
capture_numbers = Numbers(data)
print(*capture_numbers.get_numbers())
