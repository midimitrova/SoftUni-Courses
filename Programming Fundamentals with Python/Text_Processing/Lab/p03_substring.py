class Substring:

    def __init__(self, word, my_string):
        self.word = word
        self.my_string = my_string

    def find_word(self):
        while self.word in self.my_string:
            self.my_string = self.my_string.replace(self.word, '')
        return self.my_string


data = input()
my_string = input()
substring = Substring(data, my_string)
print(substring.find_word())
