from random import randint


# печать матрицы (с возможностью выделения колонки)
def print_matrix(matrix: list, col_hint: int = -1):
    for row in matrix:
        for i in range(len(row)):
            # если номер колонки соответствует номеру колонки для выделения
            if col_hint == i and col_hint != -1:
                print('\033[33m' + str(row[i]).rjust(3, ' ') + '\033[0m', end='')
            else:
                print(str(row[i]).rjust(3, ' '), end='')
        print()


def first_task(n: int):
    """
    В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.
    """

    # создаём матрицу со случайными числами
    rand_matrix = [[randint(1, 49) for _ in range(9)] for _ in range(9)]

    print_matrix(rand_matrix)

    for row in rand_matrix:
        row[n - 1] = row[n - 1] * 2
    print()

    print_matrix(rand_matrix, col_hint=n-1)


def main():
    try:
        n = int(input('Номер столбца [1-9]: '))

        # если n не в диапазоне 1..9, то возбуждаем ошибку
        if not 1 <= n <= 9:
            raise ValueError

        first_task(n=n)

    except ValueError:
        print('\033[31mНеверное число или символ!\033[0m')
        main()


if __name__ == '__main__':
    main()
