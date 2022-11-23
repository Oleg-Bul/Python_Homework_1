# 2'. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋁ - "Или"
# ⋀ - "И"
# ¬ - "Не"

print('Введите X,Y,Z (True или False, 1 или 0) для  утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ')
x = bool(input('X: '))
y = bool(input('Y: '))
z = bool(input('Z: '))

if not(x or y or z) == ((not x) and (not y) and (not z)):
    print ('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z верно')
else:
    print()
