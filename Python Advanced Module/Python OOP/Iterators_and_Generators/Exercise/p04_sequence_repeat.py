class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx_chr = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration

        self.number -= 1
        output = self.sequence[self.idx_chr]
        self.idx_chr += 1
        if self.idx_chr > len(self.sequence) - 1:
            self.idx_chr = 0
        return output


# --- test code ---
# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end ='')
#
# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end='')
