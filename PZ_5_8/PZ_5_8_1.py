def paint_stars(max_num: int) -> None:
    """
    Составить программу, в которой функция построит изображение, в котором в
    первой строке 1 звездочка, во второй - 2, в третьей -3, ..., в строке с номером m - m
    звездочек.
    """

    if max_num != 1:
        paint_stars(max_num=max_num - 1)
    print('*' * max_num)


def main() -> None:
    try:
        m = int(input('Кол-во звёздочек в последнем ряду: '))

        # если m меньше 1, то возбуждаем ошибку
        if m < 1:
            raise ValueError

        paint_stars(max_num=m)
    except ValueError:
        print('\033[31mНеверное число!\033[0m')
        main()


if __name__ == '__main__':
    main()
