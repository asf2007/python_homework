file1 = open('homeWork4/task5/file1.txt', 'r')
file2 = open('homeWork4/task5/file2.txt', 'r')
sum_file = open('homeWork4/task5/sumFile.txt', 'w')
for line in file1:
    str_poly1 = line
file1.close()
for line in file2:
    str_poly2 = line
file2.close()
def list_from_poly(str_poly) :
    str_lst = str_poly.split(" + ")
    poly_lst = []
    for i in range(len(str_lst)) :
        poly_lst.append(int(str_lst[i].split("x**")[0]))
    return poly_lst
print(list_from_poly(str_poly1))
print(list_from_poly(str_poly2))

def sum_poly(poly1, poly2) :
    sum = []
    if len(poly1) > len(poly2) :
        for i in range(len(poly2)) :
            poly1[i] += poly2[i]  
        sum = poly1
    else :
        for i in range(len(poly1)) :
            poly2[i] += poly1[i]
        sum = poly2
    return sum
print(sum_poly(list_from_poly(str_poly1), list_from_poly(str_poly2)))
sum_lst = sum_poly(list_from_poly(str_poly1), list_from_poly(str_poly2))
final_lst = []
for i in range(len(sum_lst)) :
    final_lst.append(f"{sum_lst[i]}x**{i}")
sum_file.write(" + ".join(final_lst))


