class AsciiValues:

    def __init__(self, command):
        self.values = {}
        self.command = command

    def get_ascii(self):
        for char in self.command:
            self.values[char] = ord(char)

    def display(self):
        print(self.values)


data = input().split(', ')
ascii_table = AsciiValues(data)
ascii_table.get_ascii()
ascii_table.display()
