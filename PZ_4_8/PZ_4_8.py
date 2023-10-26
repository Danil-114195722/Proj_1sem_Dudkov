def first_task():
    """
    Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел от A
    до B включительно.
    """

    a = int(input('Введите целое число A: '))
    b = int(input('Введите целое число B (B > A): '))

    # если b меньше a, то возбуждаем ошибку
    if b < a:
        raise ValueError

    sqr_sum = 0
    for i in range(a, b + 1):
        sqr_sum += i ** 2

    print('Сумма:', sqr_sum)


def second_task():
    """
    Начальный вклад в банке равен 1000 руб. Через каждый месяц размер вклада
    увеличивается на P процентов от имеющейся суммы (P — вещественное число, 0< P
    <25). По данному P определить, через сколько месяцев размер вклада превысит 1100
    руб., и вывести найденное количество месяцев K (целое число) и итоговый размер
    вклада S (вещественное число).
    """

    default_contrib = 1000

    p = float(input('Введите процент вклада [0 < P < 25] '))

    # если p не 0 < P < 25, то возбуждаем ошибку
    if p <= 0 or p >= 25:
        raise ValueError

    contrib = default_contrib
    months = 0
    while contrib <= 1100:
        contrib += contrib * (p / 100)
        months += 1

    print(f'Месяцев прошло: {months}\nИтоговый размер вклада: {contrib}')


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
