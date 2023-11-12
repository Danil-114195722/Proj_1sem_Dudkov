from random import randint


# печать матрицы
def print_matrix(matrix: list):
    for row in matrix:
        for i in range(len(row)):
            print(str(row[i]).rjust(3, ' '), end='')
        print()


def second_task():
    """
    В матрице элементы последней строки заменить на 0.
    """

    # случайная длина матрицы от 3 до 9
    matrix_len = randint(3, 9)

    # создаём матрицу со случайными числами и случайной длиной от 3 до 9
    rand_matrix = [[randint(1, 99) for _ in range(matrix_len)] for _ in range(matrix_len)]

    print_matrix(rand_matrix)

    # заменяем все элементы последней строки на 0
    rand_matrix[-1] = [0 for _ in range(matrix_len)]
    print()

    print_matrix(rand_matrix)


if __name__ == '__main__':
    second_task()
