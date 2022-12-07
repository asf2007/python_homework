num = int(input("номер четверти: "))
if num == 1 :
    print("{} -> x > 0 and y > 0 ".format(num))
elif num == 2 :
    print("{} -> x < 0 and y > 0 ".format(num))
elif num == 3 :
    print("{} -> x < 0 and y < 0 ".format(num))
elif num == 4 :
    print("{} -> x > 0 and y < 0 ".format(num))
else : 
    print("некорректное значение")