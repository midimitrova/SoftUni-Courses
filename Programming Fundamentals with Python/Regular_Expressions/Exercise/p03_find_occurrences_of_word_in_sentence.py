import re


class FindOccurrences:

    def __init__(self, text, word):
        self.text = text
        self.word = word

    def find_word(self):
        pattern = rf'{self.word}\b'
        valid_word = [el for el in re.findall(pattern, self.text, re.IGNORECASE)]
        return len(valid_word)


data = input()
searched_word = input()
find_occurrences = FindOccurrences(data, searched_word)
print(find_occurrences.find_word())
