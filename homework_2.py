number = int(input("Введите пятизначное число: "))
if 10000 <= number < 100000:  # Проверяем, что число пятизначно
# Извлекаем каждую цифру из числа
    tens_of_thousands = number // 10000
    thousands = (number % 10000) // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    units = number % 10
         
        # Выполняем расчеты по заданному алгоритму
    a = ((tens ** units) *  hundreds)/(tens_of_thousands - thousands)
    print(a)