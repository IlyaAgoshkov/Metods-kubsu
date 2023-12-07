import numpy as np

# Функция для оценки суммы ряда с заданной точностью
def estimate_series(precision):
    sum_series = 0.0
    n = 1
    while True:
        term = 1 / (n**2 + 1)
        sum_series += term
        if term < precision:
            break
        n += 1
    return sum_series, n

# Подсказка предлагает использовать известные суммы 1/n^2 и 1/n^4 для оценки ошибки
pi_squared_over_six = np.pi**2 / 6
pi_fourth_over_ninety = np.pi**4 / 90

# Расчет приблизительной оценки ошибки
def error_approximation(n):
    return (pi_squared_over_six - (1 / (n**2))) - (pi_fourth_over_ninety - (1 / (n**4)))

# Рассчитываем сумму с ошибкой меньше одной десятой
sum_result, terms_used = estimate_series(1e-1)

# Расчет приблизительной оценки ошибки
error_estimate = error_approximation(terms_used)

print(sum_result, terms_used, error_estimate)
