import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-10, 10, 400)
y1 = np.abs(np.sin(x1))
y2 = np.cos(x1)

# Первое окно с двумя графиками
plt.figure(1)
plt.subplot(211)  # 2 строки, 1 столбец, 1-й график
plt.plot(x1, y1, label='|sin(x)|')
plt.title('График функции |sin(x)|')
plt.legend()

plt.subplot(212)  # 2 строки, 1 столбец, 2-й график
plt.plot(x1, y2, label='cos(x)', color='orange')
plt.title('График функции cos(x)')
plt.legend()

# Второе окно с одним графиком
x2 = np.linspace(-10, 10, 400)
y3 = 3 * x2**2 - 13

plt.figure(2)
plt.plot(x2, y3, label='3x^2 - 13', color='green')
plt.title('График функции 3x^2 - 13')
plt.legend()


plt.show()

