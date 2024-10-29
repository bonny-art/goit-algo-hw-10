"""
Дослідження обчислення інтегралу методом Монте-Карло та порівняння з аналітичними розрахунками.

Ця програма обчислює визначений інтеграл функції f(x) = x^2 на відрізку [0, 2] 
методом Монте-Карло та порівнює результати з аналітичними розрахунками. 
Крім того, програма будує графіки для візуалізації функції та результатів методу Монте-Карло.
"""

import timeit
from integrals.analytic import calculate_analytic_integral
from integrals.monte_carlo import monte_carlo_integration
from plotting.plot_function import plot_function_without_points
from plotting.plot_monte_carlo import plot_monte_carlo_integration

def main():
    """
    Основна функція для виконання обчислень інтегралу та візуалізації результатів.

    Обчислює аналітичний інтеграл, виконує інтеграцію методом Монте-Карло з різними
    кількостями випадкових точок, виводить результати в консоль і будує графіки.
    """

    a, b = 0, 2
    points_list = [10, 100, 1000, 10000, 100000, 1000000]

    # Обчислення та відображення аналітичного інтегралу
    result, error = calculate_analytic_integral(a, b)
    print(f"\nАналітичний інтеграл: {result:.4f}")
    print(f"Оцінка похибки методом SciPy: {error:.4e}")

    # Побудова графіка функції без точок Монте Карло та збереження у файл
    plot_function_without_points(a, b, "task_02/results/function_plot.png")

    # Виконання інтеграції методом Монте Карло з різними кількостями точок
    for N in points_list:
        # Вимірювання часу, необхідного для інтеграції методом Монте Карло
        start_time = timeit.default_timer()
        integral_monte_carlo, under_curve, x_random, y_random = monte_carlo_integration(a, b, N)
        elapsed_time = (timeit.default_timer() - start_time) * 1000  # Перетворення у мілісекунди

        print(f"\nІнтеграл методом Монте-Карло (N={N}): {integral_monte_carlo:.4f}")
        print(f"Абсолютна похибка: {abs(result - integral_monte_carlo):.4f}")
        print(f"Час виконання: {elapsed_time:.2f} мс")  # Виведення в мілісекундах

        # Побудова графіків результатів Монте Карло та збереження у файл
        filename = f"task_02/results/monte_carlo_integration_N_{N}.png"
        plot_monte_carlo_integration(a, b, N, integral_monte_carlo, under_curve, x_random, y_random, filename)

if __name__ == "__main__":
    main()
