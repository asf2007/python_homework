# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
import random
sweet = 100
while sweet > 0 :
    player1 = int(input("игрок 1 взял конфет: "))
    sweet -= player1
    print(f"осталось {sweet}")
    if(sweet < 1) :
        print("p1 win!")
        break
    # player2 = int(input("игрок 2 взял конфет: "))
    if sweet > 57  :
        player2 = random.randint(1, 29)
    elif sweet < 58 and sweet > 29 :
        player2 = sweet - 29
    elif sweet < 29 :
        player2 = sweet
    print(f"игрок 2 взял конфет: {player2}")
    sweet -=player2
    print(f"осталось {sweet}")
    if(sweet < 1) :
        print("p2 win!")
        break
