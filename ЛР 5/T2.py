import random


class RandomNumberIterator:
    def __init__(self, count, range_start, range_end):
        self.count = count
        self.range_start = range_start
        self.range_end = range_end

    def __iter__(self):
        return self.generate_random_numbers()

    def generate_random_numbers(self):
        for x in range(self.count):
            yield random.randint(self.range_start, self.range_end)


if __name__ == "__main__":
    iterator = RandomNumberIterator(5, 0, 100)
    for number in iterator:
        print(number)
