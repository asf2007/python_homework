# def diff(lst) :
#     max = 0
#     min = 0
#     for i in range(len(lst)) :
#         lst[i] = lst[i] % 1
#         if lst[i] > max :
#             max = lst[i]
#         elif min > lst[i] :
#             min = lst[i]
#     diff_lst = max - min
#     return diff_lst
# lst1 = [1.1, 1.2, 3.1, 5, 10.01]
# print(diff(lst1))

lst1 = [1.1, 1.2, 3.1, 5, 10.01]
lst_double = list(map(lambda x : x % 1, lst1))
print(max(lst_double) - min(lst_double))