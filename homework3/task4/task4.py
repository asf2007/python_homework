def binary_tr (num) :
    bin_lst = []
    while num > 0 :
        bin_lst.append(str(num % 2))
        num //= 2
    return bin_lst[ :: -1]
number = int(input("Ведите число: "))
print("".join(binary_tr(number)))
