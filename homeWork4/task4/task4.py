import random
k = int(input("Введите число: "))
data = open('homeWork4/task4/file.txt', 'w')
lst = []
for i in range(0, k + 1) :
    lst.append(f"{random.randint(0, 100)}x**{i}")
data.write(" + ".join(lst))
       