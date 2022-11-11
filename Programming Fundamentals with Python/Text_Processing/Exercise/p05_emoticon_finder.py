class EmoticonFinder:

    def __init__(self, message):
        self.message = message
        self.result = ''

    def finder(self):
        for char_index in range(0, len(self.message) - 1):
            if self.message[char_index] == ':':
                result = f'{self.message[char_index]}{self.message[char_index + 1]}'
                print(result)
            self.result = ''


text = input()
emoji = EmoticonFinder(text)
emoji.finder()
