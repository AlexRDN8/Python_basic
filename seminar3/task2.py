"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai
. Последняя строка содержит число X
5
1 2 3 4 5
6
-> 5
"""

n = int(input("Введите количество элементов списка: "))
list_1 = []
for i in range(1, n+1):
    list_1.append(i)
print(list_1)
x = int(input("Введите число x: "))

min = list_1[0]
for i in range(n):
        if abs(list_1[i] - x) < abs(min - x):
            min = list_1[i]
print (f"самый близкий по величине элемент к заданному числу {x} в массиве {list_1}- это {min}")
