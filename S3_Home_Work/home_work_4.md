В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько же, сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. Студент сдал первую сессию. Какова вероятность, что он учится: 
    - a). на факультете A 
    - б). на факультете B 
    - в). на факультете C?

---

Для решения этой задачи необходимо использовать формулу Байеса:

P(A|B) = P(B|A) * P(A) / P(B),

где

P(A|B) - вероятность того, что событие A произошло при условии, что произошло событие B;
P(B|A) - вероятность того, что событие B произошло при условии, что произошло событие A;
P(A) - априорная вероятность события A;
P(B) - полная вероятность события B.
В данной задаче событие B - "студент сдал первую сессию".

Из условия задачи известно, что студентов на факультетах A и B одинаковое количество, а студентов на факультете C столько же, сколько на факультетах A и B вместе. Пусть количество студентов на каждом факультете равно n. Тогда общее количество студентов будет равно 2n + n = 3n.

Тогда априорные вероятности того, что случайно выбранный студент учится на каждом факультете будут следующими:

P(A) = n / (2n + n) = 1/3,
P(B) = n / (2n + n) = 1/3,
P(C) = 2n / (2n + n) = 2/3.

Вероятность того, что студент сдал первую сессию, можно найти как сумму вероятностей сдачи сессии на каждом из факультетов, умноженную на соответствующую априорную вероятность:

P(B) = P(A) * 0.8 + P(B) * 0.7 + P(C) * 0.9 = 0.8/3 + 0.7/3 + 1.8/3 = 2.3/3.

Тогда вероятности того, что студент, сдавший первую сессию, учится на каждом из факультетов будут равны:

P(A|B) = P(B|A) * P(A) / P(B) = 0.8/2.3,
P(B|B) = P(B|B) * P(B) / P(B) = 0.7/2.3,
P(C|B) = P(B|C) * P(C) / P(B) = 1.8/2.3.