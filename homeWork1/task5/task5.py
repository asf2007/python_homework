import math
aX = int(input("Ведите координату X точки А: "))
aY = int(input("Ведите координату Y точки А: "))
bX = int(input("Ведите координату X точки B: "))
bY = int(input("Ведите координату Y точки B: "))
distance = math.sqrt((aX - bX) ** 2 + (aY - bY) ** 2)
print(distance) 