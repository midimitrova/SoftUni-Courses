class TextFilter:

    def __init__(self, words, text):
        self.words = words
        self.text = text

    def filter(self):
        for word in self.words:
            while word in self.text:
                self.text = self.text.replace(word, '*' * len(word))
        return self.text


words_to_banned = input().split(', ')
text = input()
text_filter = TextFilter(words_to_banned, text)
print(text_filter.filter())
