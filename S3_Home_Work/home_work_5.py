print('\nУстройство состоит из трех деталей. ')
print('Для первой детали вероятность выйти из строя в первый месяц равна 0.1, ')
print('для второй - 0.2, для третьей - 0.25. ')
print('Вероятность того, что в первый месяц выйдут из строя:')

p1 = 0.1  # вероятность выхода из строя первой детали
p2 = 0.2  # вероятность выхода из строя второй детали
p3 = 0.25 # вероятность выхода из строя третьей детали

# а) Вероятность того, что все детали выйдут из строя
p_all = p1 * p2 * p3
print(f"все детали: {p_all:.3}")

# б) Вероятность того, что выйдут из строя только две детали
p_two = p1 * p2 * (1 - p3) + p1 * (1 - p2) * p3 + (1 - p1) * p2 * p3
print(f"только две детали: {p_two:.3}")

# в) Вероятность того, что хотя бы одна деталь выйдет из строя
p_one = 1 - (1 - p1) * (1 - p2) * (1 - p3)
print(f"хотя бы одна деталь: {p_one:.3}")

# г) Вероятность того, что выйдет из строя от одной до двух деталей
p_one_or_two = p_one + p_two
print(f"от одной до двух деталей: {p_one_or_two:.3}")
