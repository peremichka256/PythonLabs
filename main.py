import math
import numpy as np
import matplotlib.pyplot as plt
import random


# Вариант 2
def task1_1():
    result = (((1 * 12 + 1) / 12 + (2 * 32 + 5) / 32 + 1 / 24)
              / 9.6 + 2.13) / 0.0004
    # Вывод без форматирования
    print('Result of caluclation: ', result)
    # Вывод с точностью до
    print('Result of caluclation: {0:.2f}'.format(result))


def task1_2(l, a):
    result = 4 / 3 * pow(l, 3) * pow(math.sin(a / 2.0), 2) * math.sqrt(math.cos(a))
    print('l = ', l, '\nm = ', a, '\nResult of caluclation: ', result)


def task3_1():
    name = input('Напишите Ваше имя: ')
    age = input('Сколько Вам лет? ')
    place_of_stude = input('Где Вы учитесь? ')
    print('Вас зовут ', name, '. Вам ',
          age, ' лет и Вы учитесь в ',
          place_of_stude, '.', sep='')


def task3_2(str_1, str_2, str_3, str_4):
    #конкатенации срок
    print(str_1 + str_2)
    #повторения строк
    print(str_4 * 3)
    #обращения по индексу
    print(str_1[3])
    #извлечения среза
    print(str_1[0:8:2])
    #определения длины строки
    print('Длина строки: ', len(str_3))
    #подсчёта количества вхождений подстроки s в строку
    print(str_1.count('р', 0, len(str_1)))
    #поиска подстроки в строке
    print(str_3.find('лю'))
    # Разбиение строки по разделителю
    print(str_2.split('ё'))
    # преобразование строки к верхнему или нижнему регистру
    print(str_1.upper(), str_4.lower())


# В строке заменить все двоеточия (:) знаком процента (%). Подсчитать количество замен
def task3_3(str):
    count = str.count(':')
    print('Из строки ',str ,' было заменено ', count, ' символов \':\'')
    new_str = str.replace(':', '%')
    print('и получена строка', new_str)


def task4_1():
    a = int(input('Введите первое число '))
    b = int(input('Введите второе число '))
    if a > b:
        print('Наибольшее число: ', a)
    else:
        print('Наибольшее число: ', b)


def task4_2():
    a = int(input('Введите число '))
    if a < 0:
        print('введённое число меньше нуля')
    elif a == 0:
        print('введённое число равно нулю')
    else:
        print('введённое число больше нуля')


def task4_3():
    matrix = [-5, -1, -100, 100, 0, 16, -8, 19, 31, -70, 34]
    sum = 0
    for i in matrix:
        if i > 0:
            sum += i
    print(matrix)
    print('Сумма положительных чисел из матрицы = ', sum)


def y(value):
    return ((value ** 2 - 1) / math.log((value ** 2 - 1), math.e)) + value


def task5_2():
    while True:
        number = int(input('Введите число '))

        if number >= 2:
            for i in range(2, number + 1):
                if number % i == 0:
                    print('Наименьший натуральный делитель', i)
                    break
            break
        else:
            print('Число должно быть больше 2')


def task5_3(number_range, size):
    matrix = []
    for i in range(size):
        if i % 2 == 0:
            raw = [(int(random.random() * number_range)
                    if j % 2 == 0 else 0) for j in range(size)]
            matrix.append(raw)
        else:
            raw = [(int(random.random() * number_range)
                    if j % 2 == 1 else 0) for j in range(size)]
            matrix.append(raw)
    print(matrix)


def task5_4():
    while True:
        size = int(input('Введите размерность вводимого массива'))
        if size > 0:
            x_vector = []
            for i in range(size):
                x_vector.append(float(input()))
            print(x_vector)
            y_vectror = [y(i) for i in x_vector]
            print(y_vectror)
            plt.plot(x_vector, y_vectror)
            plt.show()
            break
        else:
            print('Введено число меньше нуля')


if __name__ == '__main__':
    button = int(input('Введите номер задания, который хотите запустить '))

    if button == 1:
        # Расчеты и вывод в терминале
        task1_1()
        # Параметры заданы в коде
        task1_2(1.7 * pow(10, 3), math.radians(18))
        task1_2(16 / 21, math.pi / 5)
    elif button == 2:
        # Расчеты в скрипте
        # Параметры вводятся с клавиатуры
        l = input("Ведите L: ")
        a = input('Введите A в градусах: ')
        task1_2(float(l), math.radians(int(a)))
    elif button == 3:
        # Работа со строками
        task3_1()
        str_1 = 'программировать'
        str_2 = 'учёба'
        str_3 = 'я люблю программировать'
        str_4 = 'ЪЪЪ'
        task3_2(str_1, str_2, str_3, str_4)
        str = "a: b: c: d% d; q:"
        task3_3(str)
    elif button == 4:
        # Ветвления, циклы
        task4_1()
        task4_2()
        task4_3()
    elif button == 5:
        x = np.array(range(-10, -2))
        #Заполнение списка с помощью обычной функции
        y_values = []
        for i in x:
            y_values.append(y(i))
        plt.plot(x, y_values)
        plt.show()

        #Заполнение списка с помощью лямбда-функции
        y_l = lambda x: ((x ** 2 - 1) / math.log(x ** 2 - 1, math.e)) + x
        y = list(map(y_l, x))
        plt.plot(x, y)
        plt.show()

        task5_2()
        task5_3(100, 5)
        task5_4()






