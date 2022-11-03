class AsciiValues:

    def __init__(self):
        self.values = {}

    def get_ascii(self):
        for char in data:
            self.values[char] = ord(char)

    def display(self):
        print(self.values)


data = input().split(', ')
ascii_table = AsciiValues()
ascii_table.get_ascii()
ascii_table.display()
