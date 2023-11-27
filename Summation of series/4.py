import math
def _err(precision):
    e = 1.0
    term = 1.0
    n = 1
    while abs(term) >= 10**(-precision):
        n += 1
        term = 1.0 / math.factorial(n**2+1)
        e += term
    return e
n = int(input("Введите кол-во операций: "))
row1 = 0
for i in range(1, n + 1):
    row1 += 1 / (math.pow(i, 2) + 1)

print("Результат обычного ряда для " + str(n) + " операций равен " + str(row1))
row2 = 0
for i in range(1, n + 1):    row2 += 1 / (math.pow(i, 4) * (math.pow(i, 2) + 1))
row2 = (math.pow(math.pi, 2) / 6) - (math.pow(math.pi, 4) / 90) + row2
print("Результат ряда с использованием преобразования для " + str(n) + " операций равен " + str(row2))
print("Разница в вычислениях составляет " + str(round(row2 - row1, 10)))
precision = 10
print()
print(f"Ошибка меньше десятого десятичного значащего разряда равна {_err(precision)}")
