def first_task():
    """
    Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел
    A и B нечетное»
    """

    a = int(input('Введите целое число A: '))
    b = int(input('Введите целое число B: '))

    if a % 2 == 1 and b % 2 == 1:
        print('Истина')
    else:
        print('Ложь')


def second_task():
    """
    Единицы длины пронумерованы следующим образом: 1 — дециметр, 2 — километр,
    3 — метр, 4 — миллиметр, 5 — сантиметр. Дан номер единицы длины (целое число
    в диапазоне 1-5) и длина отрезка в этих единицах (вещественное число). Найти
    длину отрезка в метрах
    """

    len_unit = int(input(
        'Номер единицы длины [1 — дециметр, 2 — километр, 3 — метр, 4 — миллиметр, 5 — сантиметр] '
    ))
    # если len_unit не в диапазоне 1..5, то возбуждаем ошибку
    if len_unit not in range(1, 6):
        raise ValueError("len_unit doesn't belong to range 1..5")

    lseg = int(input('Длина отрезка в выбранных единицах: '))

    if len_unit == 1:
        res = lseg / 10
    elif len_unit == 2:
        res = lseg * 1000
    elif len_unit == 4:
        res = lseg / 1000
    elif len_unit == 5:
        res = lseg / 100
    else:
        res = lseg

    print('Длина отрезка в метрах:', res)


def main():
    try:
        first_task()
    except ValueError:
        print('\033[31mНеверное число!\033[0m')
        main()

    try:
        second_task()
    except ValueError:
        print('\033[31mНеверное число!\033[0m')
        main()


if __name__ == '__main__':
    main()
