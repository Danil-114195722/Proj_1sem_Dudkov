"""
Разработать программу, выводящую на экран число, полученное при перестановке цифр сотен и десятков исходного числа.
"""


def main() -> None:
    try:
        int_num = int(input('Введите трёхзначное число: '))

        # если юзер ввёл НЕ трёхзначное число
        if len(str(int_num)) != 3:
            raise ValueError

        result = (int_num // 10 % 10 * 100) + (int_num // 100 * 10) + (int_num % 10)
        print(f'Ответ: {result}')

    # обработка ошибок
    except ValueError:
        print('Неверные данные!!!')


if __name__ == "__main__":
    main()
