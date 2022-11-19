import re


class ExtractLinks:

    def __init__(self, text):
        self.text = text
        self.valid_links = []

    def extract(self):
        pattern = r'(w{3}\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
        while self.text:
            matches = [el.group() for el in re.finditer(pattern, self.text)]
            self.valid_links.extend(matches)
            self.text = input()

        return self.valid_links


data = input()
find_link = ExtractLinks(data)
print('\n'.join(find_link.extract()))
