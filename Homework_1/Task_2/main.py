print('Напишите программу для проверки истинности утверждения ¬(X V Y V Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')

flag = True
for x in range(2):
    for y in range(2):
        for z in range(2):
            f1 = not (x or y or z)
            f2 = not (x) and not (z) and not (y)
            if f1 != f2:
                flag = False
if flag == True:
    print('Истинность проверена')
