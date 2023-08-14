try:
    input_str = input("Введите числа через запятую: ")
    array = [int(x) for x in input_str.split(',')]

    has_multiples_of_three = False

    for number in array:
        if number % 3 == 0:
            has_multiples_of_three = True
            print(number)

    if not has_multiples_of_three:
        print(f"В {array} нет чисел, кратных 3")
except ValueError:
    print(f"В массиве [{input_str}] должны быть только числа")
