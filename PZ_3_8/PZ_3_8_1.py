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


def main():
    try:
        first_task()
    except ValueError:
        print('\033[31mНеверное число!\033[0m')
        main()


if __name__ == '__main__':
    main()
