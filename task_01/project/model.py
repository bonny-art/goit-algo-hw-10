"""
Модуль для створення моделі оптимізації виробництва напоїв.

Цей модуль містить функцію `create_model`, яка створює модель оптимізації
виробництва напоїв на основі обмежених ресурсів. Модель створюється за допомогою
бібліотеки PuLP, і містить змінні для кількості вироблених одиниць напоїв, цільову
функцію максимізації виробництва, а також обмеження, що базуються на доступних ресурсах.
"""

import pulp

def create_model() -> tuple[pulp.LpProblem, pulp.LpVariable, pulp.LpVariable]:
    """
    Створює модель оптимізації виробництва напоїв.

    Модель містить змінні для кількості виробленого "Лимонаду" та "Фруктового соку",
    цільову функцію для максимізації загальної кількості вироблених напоїв і обмеження
    на ресурси.

    Returns:
        tuple: Модель лінійної оптимізації, змінна для "Лимонаду", змінна для "Фруктового соку".
    """
    model = pulp.LpProblem("Optimization_Production", pulp.LpMaximize)

    # Змінні для кількості напоїв
    lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
    fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

    # Цільова функція - максимізація виробництва напоїв
    model += lemonade + fruit_juice, "Total_Production"

    # Обмеження на доступні ресурси
    model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
    model += 1 * lemonade <= 50, "Sugar_Constraint"
    model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
    model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

    return model, lemonade, fruit_juice
