def mult_pair(lst) :
    lst_mult = []
    for i in range(0, len(lst) // 2) :
        lst_mult.append(lst[i] * lst[len(lst) - 1 - i])
        if i == ((len(lst) // 2) - 1) and (len(lst) % 2) > 0 :
            lst_mult.append(lst[len(lst) // 2] ** 2)

    return lst_mult

lst = [2, 3, 4, 5, 6]
print(mult_pair(lst))
