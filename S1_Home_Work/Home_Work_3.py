print("\nВ ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.")
print("- Какова вероятность того, что все извлеченные детали окрашены?\n")

# В данной задаче нужно найти вероятность того, что из трех извлеченных деталей все будут окрашены.
# Для этого нужно разделить число исходов, благоприятствующих этому событию, на общее число исходов.
# Общее число исходов можно найти по формуле сочетаний:
# C(15, 3) = 15! / (3! * (15 - 3)!) = 455
# Число благоприятных исходов - это число сочетаний из 9 окрашенных деталей по 3:
# C(9, 3) = 9! / (3! * (9 - 3)!) = 84
# Таким образом, вероятность того, что все три извлеченные детали окрашены, равна:
# P = 84 / 455 ≈ 0.1846
# Ответ: вероятность того, что все извлеченные детали окрашены, равна примерно 0.1846 или 18.46%.

# функция для вычисления факториала


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# функция для вычисления сочетаний


def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


# число благоприятных исходов
favourable_outcomes = combinations(9, 3)

# общее число исходов
total_outcomes = combinations(15, 3)

# вероятность того, что все три извлеченные детали окрашены
probability = favourable_outcomes / total_outcomes

print("Вероятность того, что все извлеченные детали окрашены:",
      probability,  "или ~", round(probability*100, 2), "%\n")
