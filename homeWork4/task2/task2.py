def mult(num) :
    lst = []
    d = 2
    m = num
    while d**2 <= num :
       if num % d == 0 :
            lst.append(d)
            num //= d
       else :
           d += 1
    lst.append(num)
    return lst
print(mult(int(input("введите число: "))))