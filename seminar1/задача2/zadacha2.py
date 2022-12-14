# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. НЕОБЯЗАТЕЛЬНАЯ

print('Введите число X')
x = int(input())
print('Введите число Y')
y = int(input())
print('Введите число Z')
z = int(input())
if (not (x or y or z)) == (not x and not y and not z):
    print(True)
else:
    print(False)