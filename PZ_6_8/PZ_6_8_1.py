from random import randint


def first_task():
    """
    Дан целочисленный список размера 10. Вывести все содержащиеся в данном списке
    четные числа в порядке убывания их индексов, а также их количество K.
    """

    # генератором списков создаём список с рандомными числами
    rand_list = [randint(1, 100) for _ in range(10)]

    res_list = [num for num in reversed(rand_list) if num % 2 == 0]

    print('Целочисленный список:', rand_list)
    print('Все четные числа в данном списке:', res_list)
    print('Их кол-во:', len(res_list))


def main():
    first_task()


if __name__ == '__main__':
    main()
