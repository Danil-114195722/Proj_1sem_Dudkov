"""
В соответствии с номером варианта перейти по ссылке на прототип.
Реализовать его в IDE PyCharm Community с применением пакета tk.
Получить интерфейс максимально приближенный к оригиналу.
Вариант 8 - https://i.pinimg.com/originals/73/c6/0d/73c60def8c55043f9fd27b370530a9cf.jpg
"""


import tkinter as tk
from tkinter import ttk

from datetime import datetime
from pprint import pprint


def window_deleted():
    print("Окно закрыто")
    root.quit()  # явное указание на выход из программы


def cancel():
    entry_first_name.delete(0, tk.END)
    entry_first_name.config(fg='Black')
    focus_out_entry_box(entry_first_name, entry_first_name_text)

    entry_last_name.delete(0, tk.END)
    entry_last_name.config(fg='Black')
    focus_out_entry_box(entry_last_name, entry_last_name_text)

    entry_screen_name.delete(0, tk.END)
    entry_screen_name.config(fg='Black')
    focus_out_entry_box(entry_screen_name, entry_screen_name_text)

    entry_email.delete(0, tk.END)
    entry_email.config(fg='Black')
    focus_out_entry_box(entry_email, entry_email_text)

    entry_phone.delete(0, tk.END)
    entry_phone.config(fg='Black')
    focus_out_entry_box(entry_phone, entry_phone_text)

    entry_password.delete(0, tk.END)
    entry_confirm_password.delete(0, tk.END)

    default_month.set(month_list[0])
    default_day.set(day_list[0])
    default_year.set("1985")
    default_country.set(country_list[0])

    radio_button_male.config(variable=tk.StringVar())
    radio_button_female.config(variable=tk.StringVar())
    checkbutton_terms_of_use.config(variable=tk.BooleanVar(value=False))

    print("Форма очищена\n")


def submit():
    gotten_month_num = str(month_list.index(combo_box_month.get()) + 1).rjust(2, "0")
    gotten_year = combo_box_year.get()
    gotten_day = combo_box_day.get().rjust(2, "0")
    try:
        full_date = datetime.strptime(f"{gotten_year}-{gotten_month_num}-{gotten_day}", "%Y-%m-%d")
    except ValueError:
        full_date = ""
        print("Invalid date was given!\n")

    data = {
        "first_name": entry_first_name.get(),
        "last_name": entry_last_name.get(),
        "screen_name": entry_screen_name.get(),
        "email": entry_email.get(),
        "phone": entry_phone.get(),
        "password": entry_password.get(),
        "confirm_password": entry_confirm_password.get(),
        "date_of_birth": full_date,
        "country": combo_box_country.get(),
        "gender": gender.get(),
        "terms_agree": terms_agree.get(),
    }

    pprint(data, indent=4)
    print("\n")

    cancel()


"""
-----------------
ОСНОВНЫЕ ЭЛЕМЕНТЫ
-----------------
"""


root = tk.Tk()
root.title("Sign Up")
root.geometry("560x655+700+400")  # ширина=500, высота=400, x=300, y=200
root.protocol('WM_DELETE_WINDOW', window_deleted)  # обработчик закрытия окна
root.resizable(False, False)  # размер окна НЕ может быть изменён
root.config(bg="#de8704")

for i in range(10):
    root.columnconfigure(index=i, weight=1)
for i in range(23):
    root.rowconfigure(index=i, weight=1)

main_title_label = tk.Label(root, text='Sign Up', bg="#de8704", fg="#fde82d", font=("Arial", 16))
main_frame = tk.Frame(root, bg='#222536', bd=5)
cancel_button = tk.Button(root, text='Cancel', font=("Arial", 11, "bold"), background="red", foreground="white", command=cancel)
submit_button = tk.Button(root, text='Submit', font=("Arial", 11, "bold"), background="green", foreground="white", command=submit)

main_title_label.place(x=10, y=4)
main_frame.grid(row=1, column=0, columnspan=11, rowspan=22, padx=0, pady=12, sticky="nsew")
cancel_button.grid(row=23, column=9, columnspan=1, ipadx=4, ipady=4, padx=0, pady=12)
submit_button.grid(row=23, column=10, columnspan=1, ipadx=4, ipady=4, padx=12, pady=12)


"""
----------------
ЯРЛЫКИ ДЛЯ ПОЛЕЙ
----------------
"""


first_name_label = tk.Label(root, text='First Name', bg="#222536", fg="#fde82d", font=("Arial", 11, "bold"))
first_name_label.grid(row=1, column=0, columnspan=4, rowspan=2, padx=0, pady=0, sticky="e")

last_name_label = tk.Label(root, text='Last Name', bg="#222536", fg="#fde82d", font=("Arial", 11, "bold"))
last_name_label.grid(row=3, column=0, columnspan=4, rowspan=2, padx=0, pady=0, sticky="e")

screen_name_label = tk.Label(root, text='Screen Name', bg="#222536", fg="#fde82d", font=("Arial", 11, "bold"))
screen_name_label.grid(row=5, column=0, columnspan=4, rowspan=2, padx=0, pady=0, sticky="e")

date_of_birth_label = tk.Label(root, text='Date Of Birth', bg="#222536", fg="#fde82d", font=("Arial", 11, "bold"))
date_of_birth_label.grid(row=7, column=0, columnspan=4, rowspan=2, padx=0, pady=0, sticky="e")

gender_label = tk.Label(root, text='Gender', bg="#222536", fg="#fde82d", font=("Arial", 11, "bold"))
gender_label.grid(row=9, column=0, columnspan=4, rowspan=2, padx=0, pady=0, sticky="e")

country_label = tk.Label(root, text='Country', bg="#222536", fg="#fde82d", font=("Arial", 11, "bold"))
country_label.grid(row=11, column=0, columnspan=4, rowspan=2, padx=0, pady=0, sticky="e")

email_label = tk.Label(root, text='E-mail', bg="#222536", fg="#fde82d", font=("Arial", 11, "bold"))
email_label.grid(row=13, column=0, columnspan=4, rowspan=2, padx=0, pady=0, sticky="e")

phone_label = tk.Label(root, text='Phone', bg="#222536", fg="#fde82d", font=("Arial", 11, "bold"))
phone_label.grid(row=15, column=0, columnspan=4, rowspan=2, padx=0, pady=0, sticky="e")

password_label = tk.Label(root, text='Password', bg="#222536", fg="#fde82d", font=("Arial", 11, "bold"))
password_label.grid(row=17, column=0, columnspan=4, rowspan=2, padx=0, pady=0, sticky="e")

confirm_password_label = tk.Label(root, text='Confirm Password', bg="#222536", fg="#fde82d", font=("Arial", 11, "bold"))
confirm_password_label.grid(row=19, column=0, columnspan=4, rowspan=2, padx=0, pady=0, sticky="e")


"""
-------------------
ПОЛЯ ДЛЯ ЗАПОЛНЕНИЯ
-------------------
"""


def focus_out_entry_box(widget, widget_text):
    if widget['fg'] == 'Black' and len(widget.get()) == 0:
        widget.delete(0, tk.END)
        widget['fg'] = 'Grey'
        widget.insert(0, widget_text)


def focus_in_entry_box(widget):
    if widget['fg'] == 'Grey':
        widget['fg'] = 'Black'
        widget.delete(0, tk.END)


entry_first_name_text = 'First name'
entry_first_name = tk.Entry(root, font='Arial 11', fg='Grey')
entry_first_name.insert(0, entry_first_name_text)
entry_first_name.grid(row=1, column=5, columnspan=6, rowspan=2, padx=6, pady=0, sticky="we")
entry_first_name.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_first_name))
entry_first_name.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_first_name, entry_first_name_text))

entry_last_name_text = 'Last name'
entry_last_name = tk.Entry(root, font='Arial 11', fg='Grey')
entry_last_name.insert(0, entry_last_name_text)
entry_last_name.grid(row=3, column=5, columnspan=6, rowspan=2, padx=6, pady=0, sticky="we")
entry_last_name.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_last_name))
entry_last_name.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_last_name, entry_last_name_text))

entry_screen_name_text = 'Last name'
entry_screen_name = tk.Entry(root, font='Arial 11', fg='Grey')
entry_screen_name.insert(0, entry_screen_name_text)
entry_screen_name.grid(row=5, column=5, columnspan=6, rowspan=2, padx=6, pady=0, sticky="we")
entry_screen_name.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_screen_name))
entry_screen_name.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_screen_name, entry_screen_name_text))

entry_email_text = 'E-mail'
entry_email = tk.Entry(root, font='Arial 11', fg='Grey')
entry_email.insert(0, entry_email_text)
entry_email.grid(row=13, column=5, columnspan=6, rowspan=2, padx=6, pady=0, sticky="we")
entry_email.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_email))
entry_email.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_email, entry_email_text))

entry_phone_text = 'Phone'
entry_phone = tk.Entry(root, font='Arial 11', fg='Grey')
entry_phone.insert(0, entry_phone_text)
entry_phone.grid(row=15, column=5, columnspan=6, rowspan=2, padx=6, pady=0, sticky="we")
entry_phone.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_phone))
entry_phone.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_phone, entry_phone_text))

entry_password = tk.Entry(root, font='Arial 11')
entry_password.grid(row=17, column=5, columnspan=6, rowspan=2, padx=6, pady=0, sticky="we")

entry_confirm_password = tk.Entry(root, font='Arial 11')
entry_confirm_password.grid(row=19, column=5, columnspan=6, rowspan=2, padx=6, pady=0, sticky="we")


"""
--------------
ПОЛЯ С ВЫБОРОМ
--------------
"""

month_list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
default_month = tk.StringVar(value=month_list[0])

day_list = [str(i) for i in range(1, 32)]
default_day = tk.StringVar(value=day_list[0])

year_list = [str(i) for i in range(1900, 2025)]
default_year = tk.StringVar(value="1985")

country_list = ["Россия", "Украина", "Беларусь", "Казахстан", "Другие"]
default_country = tk.StringVar(value=country_list[0])


combo_box_month = ttk.Combobox(root, values=month_list, textvariable=default_month, font='Arial 10 bold')
combo_box_month.grid(row=7, column=5, columnspan=4, rowspan=2, padx=6, pady=0, sticky="we")

combo_box_day = ttk.Combobox(root, values=day_list, textvariable=default_day, font='Arial 11', width=5)
combo_box_day.grid(row=7, column=9, columnspan=1, rowspan=2, padx=6, pady=0, sticky="we")

combo_box_year = ttk.Combobox(root, values=year_list, textvariable=default_year, font='Arial 11', width=5)
combo_box_year.grid(row=7, column=10, columnspan=2, rowspan=2, padx=6, pady=0, sticky="we")

combo_box_country = ttk.Combobox(root, values=country_list, textvariable=default_country, font='Arial 10 bold')
combo_box_country.grid(row=11, column=5, columnspan=6, rowspan=2, padx=6, pady=0, sticky="we")


"""
---------------
РАДИО И ГАЛОЧКИ
---------------
"""

male = "Мужской"
female = "Женский"
gender = tk.StringVar()
gender_style = ttk.Style()
gender_style.configure("BW.TRadiobutton", font=("Arial", 9), background="#222536", border=0, foreground="#fde82d")

radio_button_male = ttk.Radiobutton(root, text="Мужской", value="male", variable=gender, style="BW.TRadiobutton")
radio_button_male.grid(row=9, column=5, columnspan=3, rowspan=2, padx=6, pady=0, sticky="w")

radio_button_female = ttk.Radiobutton(root, text="Женский", value="female", variable=gender, style="BW.TRadiobutton")
radio_button_female.grid(row=9, column=8, columnspan=3, rowspan=2, padx=6, pady=0, sticky="w")


terms_agree = tk.BooleanVar(value=False)
terms_style = ttk.Style()
terms_style.configure("BW.TCheckbutton", font=("Arial", 9), background="#222536", border=0, foreground="#fde82d")

checkbutton_terms_of_use = ttk.Checkbutton(root, text="I agree to the Terms of Use", variable=terms_agree, style="BW.TCheckbutton")
checkbutton_terms_of_use.grid(row=21, column=5, columnspan=6, rowspan=1, padx=6, pady=0, sticky="w")

root.mainloop()
