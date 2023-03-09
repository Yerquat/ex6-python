# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def Progression(a1, d, n):
    array = []
    for i  in range(n):
        a = a1 + d * i
        array.append(a)
    return array
a1 = int(input())
d = int(input())
n = int(input())
print(Progression(a1, d, n))
