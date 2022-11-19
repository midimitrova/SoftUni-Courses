import re


class ExtractEmail:

    def __init__(self, text):
        self.text = text

    def extract(self):
        pattern = r'\s(([a-z0-9]+[a-z0-9\.\_\-]*)@[a-z\-]+(\.[a-z]+)+)\b'
        while self.text:
            matches = [el.group() for el in re.finditer(pattern, self.text)]
            return matches


data = input()
find_email = ExtractEmail(data)
print('\n'.join(find_email.extract()))
