number = int(input("Выберите число от 0 до 36: "))

if number == 0:
    print("Вы выбрали зеленый.")
elif 1 <= number <= 10:
    if number % 2 != 0:
        print("Вы выбрали красный.")
    else:
        print("Вы выбрали черный.")
elif 11 <= number <= 18:
    if number % 2 != 0:
        print("Вы выбрали черный.")
    else:
        print("Вы выбрали красный.")
elif 19 <= number <= 28:
    if number % 2 != 0:
        print("Вы выбрали красный.")
    else:
        print("Вы выбрали черный.")
elif 29 <= number <= 36:
    if number % 2 != 0:
        print("Вы выбрали черный.")
    else:
        print("Вы выбрали красный.")
else:
    print("Вы ввели неверное число! Введите число от 0 до 36.")
