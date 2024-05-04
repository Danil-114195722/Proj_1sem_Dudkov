"""
Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
Использовать модуль pickle для сериализации и десериализации объектов Python в
бинарном формате.
"""


import pickle


class Human:
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def info(self) -> None:
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")


def save_def(instance: Human, filepath: str) -> None:
    with open(filepath, "wb") as file:
        pickle.dump(obj=instance, file=file)


def load_def(filepath: str) -> Human:
    with open(filepath, "rb") as file:
        human_instance = pickle.load(file=file)
    return human_instance


if __name__ == '__main__':
    test_human = Human(name="Test", age=100500, gender="F")
    vasya = Human(name="Василий", age=25, gender="М")
    ann = Human(name="Анна", age=19, gender="Ж")

    save_def(instance=test_human, filepath="./saves/test_human.pickle")
    save_def(instance=vasya, filepath="./saves/vasya.pickle")
    save_def(instance=ann, filepath="./saves/ann.pickle")

    test_human_l = load_def(filepath="./saves/test_human.pickle")
    vasya_l = load_def(filepath="./saves/vasya.pickle")
    ann_l = load_def(filepath="./saves/ann.pickle")

    test_human_l.info()
    vasya_l.info()
    ann_l.info()
