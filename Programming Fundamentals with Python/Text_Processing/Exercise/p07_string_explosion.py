class StringExplosion:

    def __init__(self, text):
        self.text = text
        self.strength = 0
        self.new_string = ''

    def explosion(self):
        for char_index in range(len(self.text)):
            if self.text[char_index] != '>' and self.strength > 0:
                self.strength -= 1
            elif self.text[char_index] == '>':
                self.new_string += self.text[char_index]
                self.strength += int(self.text[char_index + 1])
            else:
                self.new_string += self.text[char_index]

        return self.new_string


data = input()
string_explosion = StringExplosion(data)
print(string_explosion.explosion())
