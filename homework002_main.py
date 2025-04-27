from homework002 import calc_addition, calc_subtraction, calc_division, calc_multiplication, calc_validation
import questionary


result = ''

while True:
    number_sys = input('Введите разрядность СС: ')
    while not calc_validation(number_sys):
        print('--- Разрядность СС должна быть целым числом от 2 до 36! Повторите ввод. ---')
        number_sys = input('Введите разрядность СС: ')

    number1 = input('Введите первое число: ')
    while not calc_validation(number_sys, num = number1):
        print('--- Число должно состоять только из символов 0-9 и A-V и не должно выходить за рамки заданной СС!'
              ' Повторите ввод. ---')
        number1 = input('Введите первое число: ')

    number2 = input('Введите второе число: ')
    while not calc_validation(number_sys, num = number2):
        print('--- Число должно состоять только из символов 0-9 и A-V и не должно выходить за рамки заданной СС!'
              ' Повторите ввод. ---')
        number2 = input('Введите второе число: ')

    operation = questionary.select(
        "выберите операцию:", choices=["+", "-", "/", "*"]
    ).ask()

    # operation = input('Введите операцию: ')
    # while not calc_validation(number_sys, operation = operation):
    #     print('--- Поддерживаются только операции: -, +, /, *! Повторите ввод.')
    #     operation = input('Введите операцию: ')

    number_sys = int(number_sys)
    match operation:
        case '+':
            result = calc_addition(number1, number2, number_sys)
        case '-':
            result = calc_subtraction(number1, number2, number_sys)
        case '/':
            result = calc_division(number1, number2, number_sys)
        case '*':
            result = calc_multiplication(number1, number2, number_sys)

    print('Результат: ', number1, operation, number2, '=', result)
    if int(number_sys) != 10:
        print('Результат в десятичной СС: ', int(number1, number_sys), operation, int(number2, number_sys), '=', int(result, number_sys))
    print('###########################################')