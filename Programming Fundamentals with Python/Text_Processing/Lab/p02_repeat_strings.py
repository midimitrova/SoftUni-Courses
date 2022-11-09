class RepeatStrings:

    def __init__(self, words):
        self.words = words

    def repeat(self):
        result = ''
        for word in self.words:
            result += word * len(word)
        return result


data = input().split()
repeat_string = RepeatStrings(data)
print(repeat_string.repeat())

