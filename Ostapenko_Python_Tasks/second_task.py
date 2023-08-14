try:
    name = str(input("Введите имя: "))
    if name.casefold() == "вячеслав":
        print("Привет, Вячеслав")
    else:
        print("Нет такого имени")
except Exception as e:
    print(e)