day = int(input("Ведите день недели от 1 до 7: "))
if day > 0 and day < 8 : 
    if day > 5 : 
        print("{} -> да".format(day))
    else : 
        print("{} -> нет".format(day))
else : 
    print("некорректное значение дня")