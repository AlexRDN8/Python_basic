"""
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""
first_element = int(input("Введите первый элемент арифметической прогрессии: "))
difference = int(input("Введите разность соседних элементов: "))
amount_elements = int(input("Введите количество элементов: "))

def arithmetic_progression(first_element, difference, amount_elements):
    list = []
    element = 0
    for i in range (1, amount_elements + 1):
        element = first_element + (i - 1) * difference
        list.append(element)
    return list

print(arithmetic_progression(first_element, difference, amount_elements))




