from re import sub as re_sub


def second_task():
    """
    Дана строка-предложение с избыточными пробелами между словами.
    Преобразовать ее так, чтобы между словами был ровно один пробел.
    """

    sentence = input('Предложение с лишними пробелами:\n')

    clean_sents = re_sub('\s+', ' ', sentence)
    print(f'Чистое предложение:\n{clean_sents}')


def main():
    second_task()


if __name__ == '__main__':
    main()
