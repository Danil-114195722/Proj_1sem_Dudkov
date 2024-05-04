"""
Создание базового класса "Животное" и его наследование для создания классов
"Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства,
такие как "гавкать" и "мурлыкать".
"""


class Animal:
    def __init__(self, nickname: str, sex: str, old: int):
        self.nickname = nickname
        self.sex = sex
        self.old = old

    def breathe(self):
        print(f'{self.nickname} дышит')

    def eat(self):
        print(f'{self.nickname} питается')

    def get_info(self):
        print(f'Кличка: {self.nickname}\nПол: {self.sex}\nВозраст: {str(self.old)}')


class Dog(Animal):
    def __init__(self, nickname: str, sex: str, old: int):
        super().__init__(nickname, sex, old)

    def bark(self):
        print(f'{self.nickname} гавкает')


class Cat(Animal):
    def __init__(self, nickname: str, sex: str, old: int):
        super().__init__(nickname, sex, old)

    def purr(self):
        print(f'{self.nickname} мурлычет')


if __name__ == '__main__':
    my_dog = Dog(nickname='Шарик', sex='Самец', old=8)
    my_cat = Cat(nickname='Матроскин', sex='Самец', old=5)

    my_cat.get_info()
    print()
    my_dog.get_info()
    print()

    my_dog.breathe()
    my_cat.purr()
    my_dog.bark()
    my_cat.eat()
