"""Задача 16:
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai
. Последняя строка содержит число X
5
1 2 3 4 5
3
-> 1
"""
n = int(input("Введите количество элементов списка: "))
list_1 = []
for i in range (1, n+1):
    list_1.append(i)
x = int(input("Введите число, которое требуется найти: "))
count = 0
for i in list_1:
    if x == i:
        count +=1
print (f"Число {x} встречается в массиве {list_1} {count} раз")


