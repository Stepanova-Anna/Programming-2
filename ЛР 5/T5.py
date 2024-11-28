import time
from time import perf_counter

class Timer:
    def __enter__(self):
        self.start_time = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = perf_counter()
        self.interval = self.end_time - self.start_time
        print(f'Время выполнения: {self.interval} секунд')


def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    n = 1000
    with Timer():
        fib_numbers = list(fib(n))
