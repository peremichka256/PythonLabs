import math


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
    print('Было заменено ', count, ' символов \':\'')
    new_str = str.replace(':', '%')
    print('и получена строка', new_str)


if __name__ == '__main__':
    # Расчеты и вывод в терминале
    task1_1()

    #Параметры заданы в коде
    task1_2(1.7 * pow(10, 3), math.radians(18))
    task1_2(16 / 21, math.pi / 5)

    # Расчеты в скрипте
    #Параметры вводятся с клавиатуры
    # l = input("Ведите L: ")
    # a = input('Введите A в градусах: ')
    # task1_2(float(l), math.radians(int(a)))

    # Работа со строками
    #task3_1()

    str_1 = 'программировать'
    str_2 = 'учёба'
    str_3 = 'я люблю программировать'
    str_4 = 'ЪЪЪ'
    task3_2(str_1, str_2, str_3, str_4)

    str = "a: b: c: d% d; q:"
    task3_3(str)

    # Ветвления, циклы


