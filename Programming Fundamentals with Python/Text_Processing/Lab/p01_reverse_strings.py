class ReverseString:

    def __init__(self, word):
        self.word = word

    def reverse(self):
        result = ''
        while True:
            reversed_word = self.word[::-1]
            if self.word == 'end':
                break
            print(f"{self.word} = {reversed_word}")

            self.word = input()


data = input()
reverse_string = ReverseString(data)
reverse_string.reverse()
