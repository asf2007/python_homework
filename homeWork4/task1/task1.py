import math
num_user = input("введите точность (например 0.001): ")
def get_pi(num_str) :
    num = 0
    tens = 0
    if num_str[1] == '.' :
        tens = len(num_str) - 2
        num_str = num_str[2:]
        num = int(num_str) * 10**tens  
    else : 
        num = int(num_str)
    k = 1
    sum = 0
    for i in range ( num ):
        if i % 2 == 0 :
            sum += 4 / k
        else :
            sum -= 4 / k
        k += 2
    return round(sum, tens)
print(f"полученное значение пи = {get_pi(num_user)}; реальное число пи = {math.pi}")
