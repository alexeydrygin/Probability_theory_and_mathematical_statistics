# функция для вычисления факториала
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# функция для вычисления сочетаний
def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

print("\nМонету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?")

n = 144
k = 70
p = 0.5

prob = combinations(n, k) * p ** k * (1 - p) ** (n - k)

print(f"\nВероятность выпадения орла ровно 70 раз из 144 подбрасываний: {(prob):.4}", "или ~", round(prob*100, 2), "%")



# import math

# n = 144
# k = 70
# p = 0.5

# prob = math.comb(n, k) * p ** k * (1 - p) ** (n - k)

# print("Вероятность выпадения орла ровно 70 раз из 144 подбрасываний: {:.4f}".format(prob))
