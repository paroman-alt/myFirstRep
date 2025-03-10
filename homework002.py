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
from operator import index

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


# функция начиная с заданной позиции справа налево уменьшает символы на 1 (в соответствии с СС)
# но только пока не выполнит условие для символа отличного от нуля
# функция возвращает измененную строку (ее длина остается прежней)
def get_post_borrow_value(num1, num_sys, entry):
    num1_symb_mass = [i for i in num1]
    for i in range(len(num1_symb_mass[:entry])-1, -1, -1):
        new_symb_index = (symbols.index(num1_symb_mass[i]) - 1) % num_sys
        num1_symb_mass[i] = symbols[new_symb_index]
        if num1_symb_mass[i] != symbols[num_sys-1]: # если это условие соблюдается, то символ не был "0"
            return ''.join(num1_symb_mass)
# print(get_post_borrow_value('1008000', 10, 4)) # -----> 0998000


# функция сравнивает два числа в заданной СС и возвращает большее
def get_greater_num(num1, num2, num_sys):
    num1_dec = int(num1, num_sys) # перевод числа из заданной сс (в строковом типе) в десятичную (в int)
    num2_dec = int(num2, num_sys)
    if num2_dec > num1_dec:
        return num2
    else:
        return num1


def calc_subtraction(num1, num2, num_sys):
    # не уверен, что такое использование рекурсии допустимо
    if get_greater_num(num1, num2, num_sys) == num2:
        return '-' + calc_subtraction(num2, num1, num_sys)
    result = []
    max_len_num = max(len(str(num1)), len(str(num2)))
    num1, num2 = add_nulls_for_equality(num1, num2)
    for i in range(max_len_num-1, -1, -1):
        res_symbol_index = symbols.index(num1[i]) - symbols.index(num2[i])
        res_symbol = symbols[:num_sys][res_symbol_index]
        result.append(res_symbol)
        if symbols.index(num1[i]) < symbols.index(num2[i]): # случай когда приходится "занимать" единицу из старших разрядов
            num1 = get_post_borrow_value(num1, num_sys, i)
    result = ''.join(reversed(result))
    return null_remover(result)


# print(add_nulls_for_equality('232ee1', '3213'))
# print(calc_subtraction('99009', '1018', 11))
# print(calc_validation(5, 8))