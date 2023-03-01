class reverse_iter:

    def __init__(self, data):
        self.data = list(data)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.data:
            raise StopIteration

        return self.data.pop()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
