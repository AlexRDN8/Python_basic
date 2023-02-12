"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
4 -> 1 2 3 4
9
"""
number_of_bushes = int(input("Введите количество кустов: "))
number_of_berries = []
for i in range(number_of_bushes):
    number_of_berries.append(i+1)
print(number_of_berries)

current_bush = int(input("Введите порядковый номер куста рядом с которым остановился собирающий модуль: "))
current_position = current_bush - 1
picked_berries = 0
if current_position == 0:
    picked_berries = number_of_berries [current_position] + number_of_berries [current_position + 1] + number_of_berries [-1]
elif current_position == len(number_of_berries) - 1:
    picked_berries = number_of_berries [current_position] + number_of_berries [current_position - 1] + number_of_berries [0]
else:
    picked_berries = number_of_berries [current_position] + number_of_berries [current_position + 1] + number_of_berries [current_position - 1]

print (f"Находясь около куста {current_bush} собирающий модуль соберет {picked_berries} ягод")


