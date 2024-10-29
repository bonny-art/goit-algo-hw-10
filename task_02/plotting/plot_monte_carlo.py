"""
Модуль для побудови графіків інтеграції методом Монте-Карло.

Функція `plot_monte_carlo_integration` створює графік, що показує функцію, 
випадкові точки та області під графіком для методу Монте-Карло.
"""

import matplotlib.pyplot as plt
import numpy as np
from integrals.analytic import f

def plot_monte_carlo_integration(a, b, N, integral_value, under_curve, x_random, y_random, filename):
    """ 
    Побудова графіка інтеграції методом Монте-Карло.

    Параметри:
    a (float): Початкова точка інтегрування.
    b (float): Кінцева точка інтегрування.
    N (int): Кількість випадкових точок.
    integral_value (float): Обчислене значення інтегралу.
    under_curve (ndarray): Масив індексів точок під кривою.
    x_random (ndarray): Масив випадкових x-координат.
    y_random (ndarray): Масив випадкових y-координат.
    filename (str): Ім'я файлу для збереження графіка.
    """

    # Генерація значень функції
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)
    ix = np.linspace(a, b)
    iy = f(ix)

    # Створення графіка
    _, ax = plt.subplots()

    # Графік функції та заповнення області під кривою
    ax.plot(x, y, 'r', linewidth=2)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Випадкові точки
    ax.scatter(x_random, y_random, color='blue', s=1, alpha=0.5, label="Випадкові точки")
    ax.scatter(x_random[under_curve], y_random[under_curve], color='green', s=1, alpha=0.5, label="Точки під кривою")

    # Налаштування осей та заголовку
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Інтеграл Монте-Карло з N={N} точками\nОбчислене значення: {integral_value:.4f}')
    ax.legend()
    plt.grid()

    # Збереження графіка у файл
    plt.savefig(filename, dpi=300)
    plt.close()
