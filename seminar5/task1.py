"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""
number_a = int(input("Введите число a: "))
number_b = int(input("Введите число b: "))

def exponentiation(a, b):
    if b == 0:
        return 1
    return exponentiation(a, b-1)*a

print(exponentiation(number_a, number_b))