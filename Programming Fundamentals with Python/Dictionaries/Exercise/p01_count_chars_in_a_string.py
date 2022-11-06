class CountChars:

    def __init__(self, characters_sequence):
        self.characters_sequence = characters_sequence
        self.char_dictionary = {}

    def make_dictionary(self):
        for char in self.characters_sequence:
            if char not in self.char_dictionary.keys():
                self.char_dictionary[char] = 0
            self.char_dictionary[char] += 1

    def __repr__(self):
        result = ''
        for char, occurrences in self.char_dictionary.items():
            result += f"{char} -> {occurrences}\n"
        return result


string_input = input().split()
string_sequence_without_space = ''.join(string_input)
counts_chars = CountChars(string_sequence_without_space)
counts_chars.make_dictionary()
print(counts_chars)
