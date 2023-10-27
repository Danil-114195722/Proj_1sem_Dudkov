from random import randint


# среднее арифметическое всех элементов списка
def avg(iter_list: list) -> float:
    return round(sum(iter_list) / len(iter_list), 2)


def third_task(n: int):
    """
    Дан список размера N. Заменить каждый элемент списка на среднее арифметическое
    этого элемента и его соседей.
    """

    # генератором списков создаём список с рандомными числами
    rand_list = [randint(1, 100) for _ in range(n)]

    # первый элемент
    res = [avg(rand_list[:2])]
    # все остальные элементы
    res += [
        avg(rand_list[i - 1: i + 2])
        for i in range(1, n - 1)
    ]
    # последний элемент
    res.append(avg(rand_list[-2:]))

    print('Список:', rand_list)
    print('Новый список:', res)


def main():
    try:
        n = int(input('Длина списка: '))

        # если n меньше 1, то возбуждаем ошибку
        if n < 1:
            raise ValueError

        third_task(n=n)
    except ValueError:
        print('\033[31mНеверное число!\033[0m')
        main()


if __name__ == '__main__':
    main()
