def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

def add_ten_gen(fib_gen):
    for num in fib_gen:
        yield num + 10


n = int(input('Введите количество чисел Фибоначчи: '))
fib_gen = fib(n)
result = add_ten_gen(fib_gen)

print('Числа Фибоначчи с добавлением 10:')
for value in result:
    print(value)
