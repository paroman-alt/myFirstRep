# Нужно реализовать калькулятор систем счисления (любая от 2 до 36).
# Пользователь вводит разрядность СС и нужную операцию (для упрощения пусть будет только сложение)
# После этого вводит 2 числа в нужной СС.
# 1. обеспечить валидацию ввода
# 2. обеспечить выполнение операции
# Например:
# Введите разрядность СС: 10
# Выберите операцию: +
# Введите первое число: 123
# Введите второе число: 7
# ___________
# Результат: 130

from logging import exception
from curses.ascii import isdigit
from operator import truediv

symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']

def calc_addition(num1, num2, num_sys):
    result = str()
    remaind = 0 # учет единицы в старшем разряде
    num1_reversed = str(num1)[::-1]
    num2_reversed = str(num2)[::-1]
    for i in range(0, max(len(str(num1)), len(str(num2)))):
        try:  # для случая когда числа разной длины и для уравнивания требуется добавить нули в меньшее
            num1_symbol = num1_reversed[i]
        except IndexError:
            num1_symbol = '0'
        try:
            num2_symbol = num2_reversed[i]
        except IndexError:
            num2_symbol = '0'
        index_of_sum_symbol = symbols.index(num1_symbol) + symbols.index(num2_symbol) + remaind
        remaind = index_of_sum_symbol // num_sys
        sum_symbol = symbols[index_of_sum_symbol % num_sys]
        result = sum_symbol + result
    if remaind != 0:  # для случая когда единица остается после завершения цикла (например 999 + 1)
        result = str(remaind) + result
    return result

# валидация ввода:
    # 1 - числа должны соответствовать заданной СС
    # 2 - для num001 и num002 допустим только ввод символов из списка symbols
    # 3 - для num_cap только int числа и от 2 до 36
    # 4 - для operation только "+", "-", "/", "*"
def calc_validation(num_sys, num = None, operation = None): # возвращает true если валидно и false если невалидно
    if type(num_sys) is not int or num_sys > 36 or num_sys < 2: # Основание СС должно быть целым числом от 2 до 36
        return False
    if num != None: # для того чтобы эту функцию можно было применить после ввода пользователем СС
        for digit in str(num):
            if digit not in symbols[0: num_sys]: # Число должно состоять только из символов 0-9 и A-V и не должно выходить за рамки заданной СС
                return False
    if operation != None and operation not in ["+", "-", "/", "*"]:
        return False
    return True


# print(calc_addition('8', '1', 9))
# print(calc_validation(5, 8))