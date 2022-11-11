class ReplaceChars:

    def __init__(self, message):
        self.message = message

    def replace(self):
        char_index = 0
        while char_index < len(self.message) - 1:
            if self.message[char_index] == self.message[char_index + 1]:
                symbol_to_replace = f'{self.message[char_index]}{self.message[char_index + 1]}'
                self.message = self.message.replace(symbol_to_replace, self.message[char_index])
                char_index = 0
            else:
                char_index += 1
        return self.message


text = input()
replace_chars = ReplaceChars(text)
print(replace_chars.replace())
