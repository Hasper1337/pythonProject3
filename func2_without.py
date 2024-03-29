# a(i) = a(i - 2) + (a(i - 1)/(2**(i - 1))
# a0 = a1 = 1

def resh(n):
    a = [1, 1]  # Массив для хранения значений a(i)
    for i in range(2, n + 1):  # Вычисление членов последовательности
        a.append(a[i - 2] + a[i - 1] / (2 ** (i - 1)))
    return a[n]  # Возвращение значения a(n)


print("Результат вычислений ->", resh(5))
