print("\nВ первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.")
print("Из каждого ящика вытаскивают случайным образом по два мяча.")
print("\nКакова вероятность того, что все мячи белые?")
print("Какова вероятность того, что ровно два мяча белые?")
print("Какова вероятность того, что хотя бы один мяч белый?")

p1 = 7/10 * 6/9 * 9/11 * 8/10
print("\nВероятность того, что все мячи белые: {:.4f}".format(p1), "или ~", round(p1*100, 2), "%")

p2 = (7/10 * 6/9 * 2/11 * 1/10) + (3/10 * 2/9 * 9/11 * 8/10) + (7/10 * 3/9 * 9/11 * 2/10) + (3/10 * 7/9 * 2/11 * 9/10)
print("Вероятность того, что ровно два мяча белые: {:.4f}".format(p2), "или ~", round(p2*100, 2), "%")

p3 = 1 - (3/5 * 2/4 * 2/3 * 1/2)
print("Вероятность того, что хотя бы один мяч белый: {:.4f}".format(p3), "или ~", round(p3*100, 2), "%")