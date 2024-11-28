import sys

class BatchCalculatorContextManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
            return self
        except FileNotFoundError as e:
            print(f"Ошибка: {e}", file=sys.stderr)
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            raise StopIteration
        return line.strip()


class Calculator:
    def calculate(self, expression):
        try:

            parts = expression.split()
            if len(parts) != 3:
              raise ValueError("Неверный формат ввода")
            a, operand, b = parts
            a = float(a)
            b = float(b)

            if operand == '+':
                return a + b
            elif operand == '-':
                return a - b
            elif operand == '*':
                return a * b
            elif operand == '/':
                if b == 0:
                    raise ZeroDivisionError("На ноль делить нельзя")
                return a / b
            else:
                raise ValueError(f"Введен неверный оператор: {operand}")

        except (ValueError, ZeroDivisionError) as e:
            print(f"Ошибка '{expression}': {e}", file=sys.stderr)
            return None
        except Exception as e:
           print(f"Ошибка: {e}", file=sys.stderr)
           return None


def main():
    filename = 'operations.txt'
    calculator = Calculator()
    try:
        with BatchCalculatorContextManager(filename) as bcm:
            for expression in bcm:
                result = calculator.calculate(expression)
                if result is not None:
                    print(f'Результат вычислений "{expression}": {result}')
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()