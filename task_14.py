class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.n:
            raise StopIteration
        result = 2 * self.index
        self.index += 1
        return result


evens = EvenNumbers(6)
for num in evens:
    print(num)