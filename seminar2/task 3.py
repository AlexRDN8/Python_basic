"""Задача 3: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа. """
import random
x = random.randint(0, 1000)
print (x)
y = random.randint(0, 1000)
print (y)
summa = x + y
multiply = x * y

number_x = (summa-int((summa**2-4*multiply)**0.5))//2
number_y = (summa+int((summa**2-4*multiply)**0.5))//2
print(number_x, number_y)


