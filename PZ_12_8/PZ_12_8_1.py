from random import randint


def first_task(n: int):
    """
    В последовательности на n целых элементов найти количество пар, для которых
    произведение элементов делится на 3 (элементы пары в последовательности являются
    соседними).
    """

    rand_list = [randint(1, 50) for _ in range(n)]
    print('Список:', rand_list)

    pairs = []
    for i in range(1, n):
        if (rand_list[i] * rand_list[i - 1]) % 3 == 0:
            pairs.append((rand_list[i - 1], rand_list[i]))

    print('Подходящие пары:', *pairs)


if __name__ == '__main__':
    first_task(
        n=int(input('Длина последовательности: '))
    )
