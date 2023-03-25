Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя: 
    - а). все детали 
    - б). только две детали 
    - в). хотя бы одна деталь 
    - г). от одной до двух деталей?

---

Для решения задачи воспользуемся формулами комбинаторики и вероятности.

а) Для того чтобы все детали вышли из строя в первый месяц, необходимо, чтобы вышли из строя все три детали. Так как события являются независимыми, то вероятность такого события равна произведению вероятностей выхода из строя каждой детали:
P(все детали выйдут из строя) = 0.1 * 0.2 * 0.25 = 0.005 = 0.5%.

б) Чтобы вышли из строя только две детали, необходимо, чтобы из трех деталей вышли из строя ровно две. Таких комбинаций три: первая и вторая детали, первая и третья детали, вторая и третья детали. Вероятность каждой из таких комбинаций равна произведению вероятностей выхода из строя выбранных деталей и не выхода из строя невыбранных деталей. Тогда:
P(только две детали выйдут из строя) = 0.1 * 0.2 * (1-0.25) + 0.1 * 0.25 * (1-0.2) + 0.2 * 0.25 * (1-0.1) = 0.045 = 4.5%.

в) Чтобы хотя бы одна деталь вышла из строя, необходимо, чтобы хотя бы одна деталь вышла из строя из трех возможных. Вероятность того, что ни одна деталь не выйдет из строя равна произведению вероятностей того, что каждая деталь не выйдет из строя: (1-0.1) * (1-0.2) * (1-0.25) = 0.54. Тогда вероятность того, что хотя бы одна деталь выйдет из строя, равна:
P(хотя бы одна деталь выйдет из строя) = 1 - 0.54 = 0.46 = 46%.

г) Чтобы от одной до двух деталей вышли из строя, необходимо вычесть из вероятности того, что хотя бы одна деталь выйдет из строя вероятность того, что все три детали выйдут из строя или только одна деталь выйдет из строя. Тогда:
P(от одной до двух деталей выйдут из строя) = 1 - P(все детали выйдут из строя) - P(ровно одна деталь выйдет из строя) = 1