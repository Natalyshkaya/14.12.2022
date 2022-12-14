# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


print('Введите число от 1 до 4')
number = int(input())
if number <= 0 or number > 4:
    print('введено некорректное число, попробуйте снова')
elif number == 1:
    print('x > 0 and y > 0')
elif number == 2:
    print('x < 0 and y > 0')
elif number == 3:
    print('x < 0 and y < 0')
else:
    print('x > 0 and y < 0')