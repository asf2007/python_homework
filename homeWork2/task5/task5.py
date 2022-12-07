# 5 Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint
import random

lst_mix = list(range(1, 10))
for i in range(len(lst_mix)) :
    mix_num = random.randint(0, len(lst_mix) - 1)
    lst_mix[i], lst_mix[mix_num] = lst_mix[mix_num], lst_mix[i]
print(lst_mix)