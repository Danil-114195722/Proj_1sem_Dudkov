from re import sub as re_sub


def second_task():
    """
    2. Из предложенного текстового файла (text18-8.txt) вывести на экран его содержимое,
    количество символов, принадлежащих к группе букв. Сформировать новый файл, в
    который поместить текст в стихотворной форме предварительно удалив букву «с» из
    текста.
    """

    with open('text18-8.txt', 'r', encoding='utf-8') as poetry:
        text = poetry.read()

    print(text)
    print(f'\nКол-во букв: {len(re_sub("[^а-яА-ЯёЁ]", "", text))}')

    with open('edited_poetry.txt', 'w') as edited_poetry:
        del_c_text = re_sub('[сС]', '', text)
        edited_poetry.write(del_c_text)


if __name__ == '__main__':
    second_task()
