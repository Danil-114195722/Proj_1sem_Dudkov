from re import findall


def task():
    """
    В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
    Посчитать количество полученных элементов.
    """

    with open('Dostoevsky.txt', 'r') as bio_file:
        bio = bio_file.read()
    all_works = set(findall('«[А-ЯЁ][\w\s]*»', bio))

    print('Все произведения:', ', '.join(all_works))
    print('Кол-во произведений:', len(all_works))


task()
