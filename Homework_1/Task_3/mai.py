print('Напишите программу, которая принимает на вход координаты точки (X и Y), \nпричём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, \nв которой находится эта точка (или на какой оси она находится).')


def find_coordinate(x, y):
    if x > 0 and y > 0:
        print(f'\nКоординаты "{x}" и "{y}" находятся на I четверти!')
    elif x > 0 and y < 0:
        print(f'\nКоординаты "{x}" и "{y}" находятся на II четверти!')
    elif x < 0 and y < 0:
        print(f'\nКоординаты "{x}" и "{y}" находятся на III четверти!')
    elif x < 0 and y > 0:
        print(f'\nКоординаты "{x}" и "{y}" находятся на IV четверти!')
    else:
        print('\nВы ввели не правильные данные, как мимнимум одна из координат должна быть больше нуля!')


num_1 = int(input('\nВведите координату X: '))
num_2 = int(input('Введите координату Y: '))

find_coordinate(num_1, num_2)