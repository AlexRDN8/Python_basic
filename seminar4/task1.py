"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12

"""
n = int(input("Введите количество элементов 1 списка: "))
m = int(input("Введите количество элементов 2 списка: "))
list1 = []
for i in range(n):
    element_list1 = int(input("Введите элемент первого списка: "))
    list1.append(element_list1)

list2 = []
for i in range(m):
    element_list2 = int(input("Введите элемент второго списка: "))
    list2.append(element_list2)

set1 = set(list1)
print(set1)
set2 = set(list2)
print(set2)
union_set = set1.intersection(set2)
union_list = list(union_set)
union_list.sort()
print(union_list)

