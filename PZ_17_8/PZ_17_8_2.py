"""
Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 2 – 9.
Выбранная задача: ПЗ 7, задание 1.
    Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из символов C.
"""


import tkinter as tk
from tkinter import ttk


def design(root: tk.Tk):
    def change(new_value):
        amount_label["text"] = str(round(float(new_value)))

    def check_char(new_value):
        return len(new_value) <= 1

    def calculate():
        char = char_entry.get()
        amount = round(amount_scale.get())

        if char and amount:
            result_value_label["text"] = char * amount

    root.title("Программа")
    root.geometry("500x500+700+400")
    root.resizable(False, False)
    root.config(bg="#333333")

    for i in range(10):
        root.columnconfigure(index=i, weight=1)
    for i in range(5):
        root.rowconfigure(index=i, weight=1)

    label_config = {
        "bg": "#333333",
        "fg": "white",
        "font": ("extra", 11, "bold"),
    }

    main_title_label = tk.Label(root, text='Программа', bg="#333333", fg="white", font=("extra", 18))
    main_title_label.grid(row=0, column=0, columnspan=10, rowspan=1, padx=0, pady=0, sticky="we")

    amount_title_label = tk.Label(root, text="Длина:", **label_config)
    amount_title_label.grid(row=1, column=0, columnspan=2, rowspan=1, padx=6, pady=0, sticky="w")

    default_amount = 10

    amount_label = tk.Label(root, text=str(default_amount), **label_config)
    amount_label.grid(row=1, column=2, columnspan=2, rowspan=1, padx=0, pady=0, sticky="w")

    amount_value = tk.IntVar(root, value=default_amount)
    amount_scale = ttk.Scale(root, orient=tk.HORIZONTAL, length=350, from_=1.0, to=20.0, variable=amount_value, command=change)
    amount_scale.grid(row=1, column=4, columnspan=6, rowspan=1, padx=10, pady=0, sticky="e")

    char_title_label = tk.Label(root, text="Символ:", **label_config)
    char_title_label.grid(row=2, column=0, columnspan=4, rowspan=1, padx=6, pady=0, sticky="w")

    char_validator = (root.register(check_char), "%P")

    char_entry = tk.Entry(root, **label_config, width=38, validate="key", validatecommand=char_validator)
    char_entry.grid(row=2, column=4, columnspan=6, rowspan=1, padx=10, pady=0, sticky="e")

    result_title_label = tk.Label(root, text="Результат:", **label_config)
    result_title_label.grid(row=3, column=0, columnspan=4, rowspan=1, padx=6, pady=0, sticky="w")

    result_value_label = tk.Label(root, **label_config)
    result_value_label.grid(row=3, column=4, columnspan=6, rowspan=1, padx=6, pady=0, sticky="we")

    submit_button = tk.Button(root, text='Выполнить', **label_config, command=calculate)
    submit_button.grid(row=4, column=3, columnspan=5, rowspan=1, padx=6, pady=0, sticky="we")


if __name__ == '__main__':
    window = tk.Tk()
    design(root=window)
    window.mainloop()
