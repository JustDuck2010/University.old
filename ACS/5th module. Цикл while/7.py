a =int(input())
x = 0
y = 1
i = 0
while i != a:
    b = x + y
    x = y
    y = b
    i += 1
print(x)

'Дано целое положительное число N.\
Напечатайте число Фибоначчи, которое находится в позиции числа N.\
Позиции для чисел Фибоначчи считайте от первого числа 1, то есть 1, 1, 2, 3, 5, 8, 13, 21, 34, ...'