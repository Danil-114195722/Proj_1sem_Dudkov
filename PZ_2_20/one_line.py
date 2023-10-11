print((lambda num: f'Ответ: {num[1] + num[0] + num[2]}' if (num.isdigit() and len(num) == 3) else 'Неверные данные')(input('Введите трёхзначное число: ')))  # 2 PZ в 1 строку для крутых
