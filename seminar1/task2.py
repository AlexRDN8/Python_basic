"""
Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10
"""
s = int(input("Введите общее количество сделанных журавликов: "))
petr = s // 6
sergey = s // 6
kate =  4 * s // 6

print(f"Петя сделал {petr} журавликов")
print(f"Сергей сделал {sergey} журавликов")
print(f"Катя сделала {kate} журавликов")