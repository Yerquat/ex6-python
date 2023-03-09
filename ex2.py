# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def Range(min, max, n, array):
    i = 0
    array1 = []
    for i in range(n):
        if min <= array[i] <= max:
            array1.append(i)
    return(array1)
    
min = int(input())
max = int(input())
n = int(input())
array = []
for i in range(n):
    a = int(input('Введите эелемент массива: '))
    array.append(a)
print(array)
print(Range(min, max, n, array))

