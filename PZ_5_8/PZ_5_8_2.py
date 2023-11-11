def add_left_digit(d: int, num: int):
    """
    Описать функцию AddLeftDigit(D, K), добавляющую к целому положительному
    числу K слева цифру D (D — входной параметр целого типа, лежащий в диапазоне
    1-9, K — параметр целого типа, являющийся одновременно входным и выходным).
    С помощью этой функции последовательно добавить к данному числу K слева
    данные цифры D1 и D2, выводя результат каждого добавления.
    """
    return int(str(d) + str(num))


def main():
    try:
        k = int(input('Число: '))
        d = int(input('Первая цифра для добавления: '))
        # если d не в диапазоне 1..9, то возбуждаем ошибку
        if not (0 < d < 10):
            raise ValueError

        res = add_left_digit(d=d, num=k)
        print(res)

        d = int(input('Вторая цифра для добавления: '))
        # если d не в диапазоне 1..9, то возбуждаем ошибку
        if not (0 < d < 10):
            raise ValueError

        res = add_left_digit(d=d, num=res)
        print(res)

    except ValueError:
        print('\033[31mНеверные данные!\033[0m')
        main()


if __name__ == '__main__':
    main()
