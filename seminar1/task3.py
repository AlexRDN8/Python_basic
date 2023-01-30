"""
Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
которая проверяет счастливость билета.
385916 -> yes
123456 -> no
"""
yourTicket = int(input("Введите шестизначное число: "))
ticket = yourTicket

sumOfLast3numbers = 0
while ticket >= 1000:
    x = ticket % 10
    sumOfLast3numbers = sumOfLast3numbers + x
    ticket = ticket // 10
#print(sumOfLast3numbers)

sumOfFirst3numbers = 0
while ticket > 0:
    x = ticket % 10
    sumOfFirst3numbers = sumOfFirst3numbers + x
    ticket = ticket // 10
#print(sumOfFirst3numbers)

if sumOfLast3numbers == sumOfFirst3numbers:
    print(f"Поздравляем, билет {yourTicket} счастливый")
else:
    print(f"К сожалению, билет {yourTicket} не является счастливый")
