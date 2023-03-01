class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next_value = self.start

    def __iter__(self):
        return self

    def __next__(self):

        if self.next_value > self.end:
            raise StopIteration

        result = self.next_value
        self.next_value += 1
        return result


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
