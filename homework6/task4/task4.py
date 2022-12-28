# import random
# k = int(input("Введите число: "))
# data = open('homeWork4/task4/file.txt', 'w')
# lst = []
# for i in range(0, k + 1) :
#     lst.append(f"{random.randint(0, 100)}x**{i}")
# data.write(" + ".join(lst))

import random
k = int(input("Введите число: "))
data = open('homeWork6/task4/file.txt', 'w')
lst = [f"{random.randint(0, 100)}x**{i}" for i in range(0, k + 1)]
data.write(" + ".join(lst))