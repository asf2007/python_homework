lst = [1, 1, 3, 1, 5, 5, 6]
def uniq_lst(lst) :
    lst_uniq = []   
    for i in lst :
        if lst.count(i) == 1 :
            lst_uniq.append(i)
    return lst_uniq
print(uniq_lst(lst))    
        