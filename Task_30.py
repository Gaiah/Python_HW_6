# Задача 30: Заполните список элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с
# новой строки.

a_1, d, qnt, li = int(input('Input a1: ')), int(input('Input d: ')), int(input('Input qnt: ')), []

li = [a_1 + (i - 1) * d for i in range(1, qnt + 1)]

print(li)