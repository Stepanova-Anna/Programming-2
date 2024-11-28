import random

class RandomNumberIterator:
    def __init__(self, count, range_tuple):
        self.count = count  # Количество случайных чисел для генерации
        self.range_tuple = range_tuple  # Диапазон (min, max)
        self.generated_numbers = 0  # Подсчет сгенерированных чисел

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated_numbers < self.count:
            random_number = random.randint(self.range_tuple[0], self.range_tuple[1])
            self.generated_numbers += 1
            return random_number
        else:
            raise StopIteration  # Завершение итерации

# Пример использования
if __name__ == "__main__":
    random_numbers = RandomNumberIterator(5, (1, 100))
    for number in random_numbers:
        print(number)
