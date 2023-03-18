import math

# Дана выборка
sample = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

# Среднее арифметическое
mean = sum(sample) / len(sample)
print("Среднее арифметическое:", mean)

# Отклонения от среднего арифметического
deviations = [x - mean for x in sample]

# Квадраты отклонений
squared_deviations = [dev**2 for dev in deviations]

# Среднее арифметическое квадратов отклонений
variance = sum(squared_deviations) / len(sample)
print("Смещенная оценка дисперсии:", variance)

# Среднее квадратичное отклонение
standard_deviation = math.sqrt(variance)
print("Среднее квадратичное отклонение:", standard_deviation)

# Несмещенная оценка дисперсии
unbiased_variance = sum(squared_deviations) / (len(sample) - 1)
print("Несмещенная оценка дисперсии:", unbiased_variance)
