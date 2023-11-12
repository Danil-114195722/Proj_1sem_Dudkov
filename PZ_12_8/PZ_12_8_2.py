from re import match as re_match


def second_task(text: str):
    """
    Составить генератор (yield), который преобразует все буквенные символы в
    заглавные.
    """

    for letter in text:
        if re_match('[a-zа-яё]', letter):
            yield letter.upper()
        else:
            yield letter


def main():
    entered_text = input('Введите строку: ')

    res_str = ''
    for i in second_task(text=entered_text):
        res_str += i

    print('результат:', res_str)


if __name__ == '__main__':
    main()
