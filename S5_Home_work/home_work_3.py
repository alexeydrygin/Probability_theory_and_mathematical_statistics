import math
import numpy as np
from scipy.stats import t

# задаем выборку весов пачек печенья
weights = np.array([202, 203, 199, 197, 195, 201, 200, 204, 194, 190])

# задаем уровень значимости alpha и доверительную вероятность
alpha = 0.01 # двусторонний тест
confidence_level = 1 - alpha

# считаем выборочное среднее, выборочное стандартное отклонение и размер выборки
sample_mean = weights.mean()
sample_std = weights.std(ddof=1)
n = len(weights)

# задаем нулевую гипотезу (H0: средний вес пачки равен 200 г) и альтернативную гипотезу (H1: средний вес пачки не равен 200 г)
mu0 = 200
H0 = 'Средний вес пачки равен {}'.format(mu0)
H1 = 'Средний вес пачки не равен {}'.format(mu0)

# считаем статистику t и соответствующее p-value
t_value = (sample_mean - mu0) / (sample_std / math.sqrt(n))
p_value = 2 * (1 - t.cdf(abs(t_value), n-1))

# считаем критическое значение t и проверяем, попадает ли статистика t в критическую область
t_critical = t.ppf(1 - alpha/2, n-1)
if abs(t_value) > t_critical:
    print('Статистика t = {} попадает в критическую область, поэтому отвергаем нулевую гипотезу.'.format(t_value))
else:
    print('Статистика t = {} не попадает в критическую область, поэтому принимаем нулевую гипотезу.'.format(t_value))

# выводим результаты теста
print('Нулевая гипотеза: {}'.format(H0))
print('Альтернативная гипотеза: {}'.format(H1))
print('Уровень значимости alpha =', alpha)
print('Доверительная вероятность:', confidence_level)
print('Выборочное среднее =', sample_mean)
print('Выборочное стандартное отклонение =', sample_std)
print('Статистика t =', t_value)
print('Критическое значение t =', t_critical)
print('p-value =', p_value)


# Статистика t = -1.0651074037450896 не попадает в критическую область, поэтому принимаем нулевую гипотезу.
# Нулевая гипотеза: Средний вес пачки равен 200
# Альтернативная гипотеза: Средний вес пачки не равен 200
# Уровень значимости alpha = 0.01
# Доверительная вероятность: 0.99
# Выборочное среднее = 198.5
# Выборочное стандартное отклонение = 4.453463071962462
# Статистика t = -1.0651074037450896
# Критическое значение t = 3.2498355440153697
# p-value = 0.31456660352472854