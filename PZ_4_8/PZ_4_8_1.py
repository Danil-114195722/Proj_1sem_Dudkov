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


def main():
    try:
        first_task()
    except ValueError:
        print('\033[31mНеверное число!\033[0m')
        main()


if __name__ == '__main__':
    main()
