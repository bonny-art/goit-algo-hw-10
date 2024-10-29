"""
Модуль для розв'язання задачі оптимізації виробництва, використовуючи методи бібліотеки PuLP.

Функції:
- solve_model: розв'язує оптимізаційну модель та повертає статус розв'язання.
"""

import pulp

def solve_model(model: pulp.LpProblem) -> str:
    """
    Розв'язує оптимізаційну модель та повертає статус розв'язання.
    
    Parameters:
    model (pulp.LpProblem): Оптимізаційна модель, яка має бути розв'язана.
    
    Returns:
    str: Статус розв'язання моделі (наприклад, 'Optimal' або інший статус).
    """
    model.solve()
    return pulp.LpStatus[model.status]
