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
from math import remainder

symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']


# функция добавляет нули в начало меньшей из двух строк для уравнивания их по длине
def add_nulls_for_equality(str1, str2):
    str1, str2 = str(str1), str(str2)
    len_dif = max(len(str1), len(str2)) - min(len(str1), len(str2))  # разница в длине строк
    nulls = '0' * len_dif # строка из нулей необходимой длины
    if len(str1) > len(str2):
        str2 = nulls + str2
    else:
        str1 = nulls + str1
    return str1, str2
# еще нашел метод zfill который нулями строку дополняет
# string.zfill('1', 4) ----> '0001'


# функция стирает из начала строки нули если они есть
def null_remover(str1):
    i = 0
    while str1[i] == '0':
        i += 1
    return str1[i:]


def calc_addition(num1, num2, num_sys):
    result = []
    remaind = 0 # учет единицы в старшем разряде
    max_len_num = max(len(str(num1)), len(str(num2)))
    num1, num2 = add_nulls_for_equality(num1, num2)
    for i in range(max_len_num-1, -1, -1):
        index_of_sum_symbol = symbols.index(num1[i]) + symbols.index(num2[i]) + remaind
        remaind = index_of_sum_symbol // num_sys
        sum_symbol = symbols[index_of_sum_symbol % num_sys]
        result.append(sum_symbol)
    if remaind != 0:  # для случая когда единица остается после завершения цикла (например 999 + 1)
        result.append(str(remaind))
    result = ''.join(reversed(result))
    return result


# валидация ввода:
    # 1 - числа должны соответствовать заданной СС
    # 2 - для num1 и num2 допустим только ввод символов из списка symbols
    # 3 - для num_sys только int числа и от 2 до 36
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


def from_symbols_multiplication_to_addition(num1, num2, num_sys):
    if len(num1) > 1 or len(num2) > 1:
        return
    res = '0'
    for i in range(symbols.index(num1)):
        res = calc_addition(res, num2, num_sys)
    return res


def calc_multiplication(num1, num2, num_sys):
    res = '0'
    for i in range(len(num2) -1, -1, -1):
        ans = '0'
        for j in range(len(num1) -1, -1, -1):
            two_symb_sum = from_symbols_multiplication_to_addition(num1[j], num2[i], num_sys)
            two_symb_sum += '0' * (len(num1)-1 - j)
            ans = calc_addition(ans, two_symb_sum, num_sys)
            # print('i =', i, 'j =', j, '   ', num1[j], '*', num2[i], '= two_symb_sum =', two_symb_sum, '    ans =', ans)
        ans += '0' * (len(num2)-1 - i) # когда в столбик умножаешь, полученные слагаемые каждый раз сдвигаются на разряд
        res = calc_addition(res, ans, num_sys)
    return res


# print(from_symbols_multiplication_to_addition('F', 'F', 16))
# print(add_nulls_for_equality('232ee1', '3213'))
# print(calc_addition('0', '1', 9))
print(calc_multiplication('ZZ', 'ZX003', 36))
# print(calc_validation(5, 8))