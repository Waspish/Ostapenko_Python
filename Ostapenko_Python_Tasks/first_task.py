try:
    number = int(input("Введите число: "))
    if number > 7:
        print("Привет")
    elif number == 7:
        print(f"Число {number} равно 7")
    else:
        print(f"Число {number} меньше 7")
except ValueError:
    print("Не является числом")
