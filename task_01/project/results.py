"""
Модуль для виведення результатів оптимізаційної моделі виробництва.
Містить функцію для виведення статусу розв'язання та кількості вироблених продуктів.
"""

import pulp

def print_results(lemonade: pulp.LpVariable, fruit_juice: pulp.LpVariable, model: pulp.LpProblem) -> None:
    """
    Виводить результати розв'язання моделі оптимізації.

    Параметри:
    lemonade (pulp.LpVariable): Змінна моделі, що представляє кількість виробленого лимонаду.
    fruit_juice (pulp.LpVariable): Змінна моделі, що представляє кількість виробленого фруктового соку.
    model (pulp.LpProblem): Оптимізаційна модель виробництва.

    Повертає:
    None
    """
    print("Статус розв'язання:                        ", pulp.LpStatus[model.status])
    print("Кількість виробленого Лимонаду:            ", lemonade.varValue)
    print("Кількість виробленого Фруктового соку:     ", fruit_juice.varValue)
    print("Максимальна кількість продуктів:           ", pulp.value(model.objective))
