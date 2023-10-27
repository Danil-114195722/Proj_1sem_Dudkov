def first_task(n: int, c: str):
    """
    Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из
    символов C.
    """
    print()
    print(c * n)


def main():
    try:
        n = int(input('Число: '))

        # если n меньше или равно 0, то возбуждаем ошибку
        if n <= 0:
            raise ValueError

        c = input('Символ: ')

        # если было введено больше/меньше 1 символа, то возбуждаем ошибку
        if len(c) != 1:
            raise ValueError

        first_task(n=n, c=c)
    except ValueError:
        print('\033[31mНеверное число или символ!\033[0m')
        main()


if __name__ == '__main__':
    main()
