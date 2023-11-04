from random import randint


def second_task(n: int):
    """
    Дан список размера N. Найти количество участков, на которых его элементы
    монотонно возрастают.
    """

    # генератором списков создаём список с рандомными числами
    rand_list = [randint(1, 100) for _ in range(n)]

    count = 0

    for i in range(2, n):
        if (rand_list[i - 2] < rand_list[i - 1]) and (rand_list[i - 1] > rand_list[i]):
            count += 1

    # проверка предпоследнего и последнего элементов
    if rand_list[n - 2] < rand_list[n - 1]:
        count += 1

    print('Список:', rand_list)
    print('Количество участков, на которых его элементы монотонно возрастают:', count)


def main():
    try:
        n = int(input('Длина списка: '))

        # если n меньше 1, то возбуждаем ошибку
        if n < 1:
            raise ValueError

        second_task(n=n)
    except ValueError:
        print('\033[31mНеверное число!\033[0m')
        main()


if __name__ == '__main__':
    main()
