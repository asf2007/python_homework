def sum_lst(lst) :
    sum = 0
    for i in range(1, len(lst), 2) :
        sum += lst[i]
    return sum
lst1 = [2, 3, 5, 9, 3]
print(sum_lst(lst1))
    