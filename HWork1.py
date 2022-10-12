import math

#----------------------------
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
def CaseProgramm1():
    num_day = int(input('введите номер дня недели 1-7: '))
    if 1 <= num_day <= 5:
        print ('No')
    elif num_day == 6 or num_day == 7:
        print ('Yes')
    else:
        print ('Не верное число')

#----------------------------
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def CaseProgramm2():
    for x in range (2):
        for y in range (2):
            for z in range (2):          
                print (f'x = {x}; y = {y}; z = {z}; == { not (x or y or z) == (not(x) and not(y) and not(z)) } ')

#----------------------------
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
def CaseProgramm3():
    coordinate_X = int(input ('Введите координату X: '))
    coordinate_Y = int(input ('Введите координату Y: '))  

    if coordinate_X > 0 and coordinate_Y > 0:
        print ('Ответ: 1')
    elif coordinate_X < 0 and coordinate_Y > 0:
        print ('Ответ: 2')
    elif coordinate_X < 0 and coordinate_Y < 0:
        print ('Ответ: 3')
    elif coordinate_X > 0 and coordinate_Y < 0:
        print ('Ответ: 4')
    elif coordinate_X == 0 and coordinate_Y == 0:
        print ('Ответ: Точка в начале координат')
    elif coordinate_X == 0:
        print ('Ответ: Точка на оси Y')
    elif coordinate_Y == 0:
        print ('Ответ: Точка на оси X')

#----------------------------
# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
def CaseProgramm4():
    surface_num = input ('Введите номер плоскости: ')

    if surface_num == '1':
        print ('X > 0 \nY > 0')
    elif surface_num == '2':
        print ('X < 0 \nY > 0')
    elif surface_num == '3':
        print ('X < 0 \nY < 0')
    elif surface_num == '4':
        print ('X > 0 \nY < 0')
    else:
        print ('Не верное значение')
    
#----------------------------
# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.    
def CaseProgramm5():
    coordinate_X1 = int(input ('Введите координату X1: '))
    coordinate_Y1 = int(input ('Введите координату Y1: '))  
    coordinate_X2 = int(input ('Введите координату X2: '))
    coordinate_Y2 = int(input ('Введите координату Y2: ')) 
    # print (f'Ответ: {round(math.sqrt((coordinate_X2 - coordinate_X1)**2 + (coordinate_Y2 - coordinate_Y1)**2), 2)}')
    print (f'Ответ: {round(((coordinate_X2 - coordinate_X1)**2 + (coordinate_Y2 - coordinate_Y1)**2)**0.5, 2)}') #попробовал такой подход, так как возведение в степень в Python выполняется без вызова функции.

#----------------------------
begin = True
while begin:

    print ('------ \n Введите число для соответствующей задачи или иное для выхода: ')
    print ('   1.\t Принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.')
    print ('   2.\t Проверка истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')
    print ('   3.\t Принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, \n\tв которой находится эта точка (или на какой оси она находится).')
    print ('   4.\t По заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).')
    print ('   5.\t Принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.')

    program = int(input())
    print ()

    if program == 1:
        CaseProgramm1()
    elif program == 2:
        CaseProgramm2()
    elif program == 3:
        CaseProgramm3()
    elif program == 4:
        CaseProgramm4()
    elif program == 5:
        CaseProgramm5()
    else:
        begin = False
