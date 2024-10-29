"""
Модуль для побудови графіка функції та області під графіком для інтегрування.
"""

import numpy as np
import matplotlib.pyplot as plt
from integrals.analytic import f

def plot_function_without_points(a, b, filename):
    """
    Побудова графіка функції f(x) на заданому відрізку [a, b].
    
    Параметри:
    a (float): Ліва межа інтегрування.
    b (float): Права межа інтегрування.
    filename (str): Назва файлу для збереження графіка.
    """

    # Генерація значень x на відрізку [-0.5, 2.5]
    x = np.linspace(-0.5, 2.5, 400)
    # Обчислення значень функції f(x)
    y = f(x)

    # Визначення точок для заповнення області під графіком
    ix = np.linspace(a, b)
    iy = f(ix)

    # Створення підграфіка
    ax = plt.subplots()[1]

    # Побудова графіка функції
    ax.plot(x, y, 'r', linewidth=2)
    # Заповнення області під графіком
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування меж осей
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання вертикальних ліній для меж інтегрування
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')

    # Додавання сітки та збереження графіка
    plt.grid()
    plt.savefig(filename, dpi=300)
    plt.close()
