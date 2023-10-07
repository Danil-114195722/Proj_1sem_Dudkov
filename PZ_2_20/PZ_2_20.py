def main() -> None:
	num = input('Введите трёхзначное число: ')

	# если юзер ввёл трёхзначное число
	if num.isdigit() and len(num) == 3:
		result = num[1] + num[0] + num[2]
		print(f'Ответ: {result}')
	else:
		print('Неверные данные!!!')


if __name__ == "__main__":
	main()
