from random import randint


def first_task():
    """
    1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
    последовательность из целых положительных и отрицательных чисел. Сформировать
    новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
    обработку элементов:

    Исходные данные:
    Количество элементов:
    Индекс последнего минимального элемента:
    Сумма элементов больших 10 во второй половине:
    """

    # добавляем в файл nums.txt случайные числа
    with open('nums.txt', 'w') as nums_file:
        rand_list = [randint(-50, 51) for _ in range(randint(10, 21))]
        for num in rand_list:
            nums_file.write(f'{num}\n')

    # читаем добавленные в файл nums.txt числа
    with open('nums.txt', 'r') as nums_file:
        nums_from_file = [int(elem.strip()) for elem in nums_file.readlines()]

    # делаем обработку элементов
    count = len(nums_from_file)
    min_index = [i for i in range(len(nums_from_file)) if nums_from_file[i] == min(nums_from_file)][-1] + 1
    sum_gt_10 = sum([num for num in nums_from_file[int(len(nums_from_file) / 2):] if num > 10])

    res_str = f'''Исходные данные: в файле nums.txt
Количество элементов: {count}
Индекс последнего минимального элемента: {min_index}
Сумма элементов больших 10 во второй половине: {sum_gt_10}'''

    # записываем обработанные данные в файл report.txt
    with open('report.txt', 'w') as report_file:
        report_file.write(res_str)


if __name__ == '__main__':
    first_task()
