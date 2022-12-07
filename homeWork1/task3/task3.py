x = int(input("Введите координату X: "))
y = int(input("Введите координату Y: "))
if x > 0 and y > 0 :
    print("x = {}; y = {}; -> 1 ".format(x, y))
elif x > 0 and y < 0 :
    print("x = {}; y = {}; -> 4 ".format(x, y))
elif x < 0 and y < 0 :
    print("x = {}; y = {}; -> 3 ".format(x, y))
elif x < 0 and y > 0 :
    print("x = {}; y = {}; -> 2 ".format(x, y))
else : 
    print("некорректное значение")