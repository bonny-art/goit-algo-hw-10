"""
Модуль для оптимізації виробництва напоїв з використанням лінійного програмування.
Визначає, яку кількість "Лимонаду" та "Фруктового соку" потрібно виробити для максимізації
загальної кількості продуктів, враховуючи обмеження на ресурси.
"""

from project.model import create_model
from project.solver import solve_model
from project.results import print_results

def main() -> None:
    """
    Основна функція, що виконує оптимізаційну модель для визначення
    кількості продуктів, які можна виробити для максимізації загальної продукції.
    """
    model, lemonade, fruit_juice = create_model()
    status = solve_model(model)
    if status == "Optimal":
        print_results(lemonade, fruit_juice, model)
    else:
        print("Не вдалося знайти оптимальне рішення.")

if __name__ == "__main__":
    main()
