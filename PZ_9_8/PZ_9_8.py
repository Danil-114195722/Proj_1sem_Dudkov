from re import split as re_split


# возвращает среднее значение по продажам
def sale_avg(sale_dict: dict) -> float:
    values_list = list(sale_dict.values())
    return sum(values_list) / len(values_list)


def task():
    """
    Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
    отражающая продажи продукции по дням в кг. Преобразовать информацию из
    строки в словари, с использованием функции найти среднее значение продаж по
    каждому виду продукции, результаты вывести на экран.
    """

    default_str = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'

    # выбираем из строки только значения продажи продукции по дням
    oranges_profits, apples_profits = re_split('[а-яА-ЯёЁ]\s|\s[а-яА-ЯёЁ]', default_str)[1::2]

    # делаем словари при помощи генераторов
    oranges = {enum: int(elem) for enum, elem in enumerate(oranges_profits.split(), start=1)}
    apples = {enum: int(elem) for enum, elem in enumerate(apples_profits.split(), start=1)}

    # ищем средние значения по продажам
    apples_avg = sale_avg(apples)
    oranges_avg = sale_avg(oranges)

    print('Продажи апельсинов:', oranges)
    print('Продажи яблок:', apples)
    print()
    print('Среднее значение по продажам апельсинов:', oranges_avg)
    print('Среднее значение по продажам яблок:', apples_avg)


if __name__ == '__main__':
    task()
