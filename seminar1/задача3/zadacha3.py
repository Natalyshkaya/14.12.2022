# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

print('Введите число X')
x = int(input())
print('Введите число Y')
y = int(input())
if x == 0 and y == 0:
    print('точка не принадлежит ни одной четверти плоскости')
elif x > 0 and y > 0:
    print('точка находится в первой четверти')
elif x < 0 and y > 0:
    print('точка находится во второй четверти')
elif x < 0 and y < 0:
    print('точка находится в третьей четверти')
else:
    print('точка находится в четвертой четверти')
