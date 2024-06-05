# Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
# оформленный согласно требованиям. Все задания выполняются c использованием модуля OS:

# 1. перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
# вложенных подкаталогов выводить не нужно.

# 2. перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
# test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
# Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
# файлов в папке test.

# 3. перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
# консоль. Использовать функцию basename() (os.path.basename()).

# 4. перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
# привязанной к нему программе. Использовать функцию os.startfile().

# 5. удалить файл test.txt.


import os
from time import sleep


def files_list(directory: str) -> None:
    for file in os.listdir(directory):
        print(file)
    print()


def first():
    print("Current path:", os.getcwd())
    os.chdir("/home/danil/Documents/RKSI/Base_of_programming/Proj_1sem_Dudkov/PZ_11_8")
    print("Path after \"cd\":", os.getcwd())

    print("List of files:\n")
    files_list(directory=".")


def second(sleep_time: int):
    os.chdir("/home/danil/Documents/RKSI/Base_of_programming/Proj_1sem_Dudkov")
    print("Current path:", os.getcwd())

    test = "./test"
    test1 = "./test/test1"

    if not os.path.isdir(test):
        os.mkdir(test)
    if not os.path.isdir(test1):
        os.mkdir(test1)

    os.replace("./PZ_6_8/PZ_6_8_1.py", f"{test}/PZ_6_8_1.py")
    os.replace("./PZ_6_8/PZ_6_8_2.py", f"{test}/PZ_6_8_2.py")
    os.replace("./PZ_7_8/PZ_7_8_1.py", f"{test1}/test.txt")

    print(f"List of files in {test}:\n")
    files_list(directory=test)

    print(f"List of files in {test1}:\n")
    files_list(directory=test1)

    print(f"Info about files in {test}:\n")
    for file in os.listdir(test):
        # проверка на то, файл или папка
        if os.path.isfile(f'{test}/{file}'):
            print(f"{test}/{file}: {os.stat(f'{test}/{file}').st_size} bytes")

    sleep(sleep_time)
    os.replace(f"{test}/PZ_6_8_1.py", "./PZ_6_8/PZ_6_8_1.py")
    os.replace(f"{test}/PZ_6_8_2.py", "./PZ_6_8/PZ_6_8_2.py")
    os.replace(f"{test1}/test.txt", "./PZ_7_8/PZ_7_8_1.py")


def third():
    os.chdir("/home/danil/Documents/RKSI/Base_of_programming/Proj_1sem_Dudkov/PZ_11_8")
    print(f"Current path: {os.getcwd()}\n")

    print(f"List of files in .:\n")
    files_list(".")

    min_filename = min(os.listdir("."), key=lambda filename: len(os.path.basename(filename)))
    print(f"Filename with min length: {min_filename}")


def fourth():
    os.chdir("/home/danil/Documents/RKSI/Base_of_programming/Proj_1sem_Dudkov/Reports")
    print(f"Current path: {os.getcwd()}\n")

    os.system("evince ./PZ_17_8.pdf")


def fifth():
    os.chdir("/home/danil/Documents/RKSI/Base_of_programming/Proj_1sem_Dudkov/test")
    print(f"Current path: {os.getcwd()}\n")

    os.system("touch ./test.txt")

    print(f"List of files in .:\n")
    files_list(".")

    os.remove("./test.txt")

    print(f"List of files after removing:\n")
    files_list(".")


if __name__ == "__main__":
    # first()
    # second(sleep_time=2)
    # third()
    fourth()
    # fifth()
