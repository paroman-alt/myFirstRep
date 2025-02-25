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


# идея 1 - переводить в 10ичную СС, выполнять операцию и переводить результат обратно в заданную СС
# (просто и неинтересно)

# идея 2 - реализовать алгоритм как считал бы вручную, складывая в столбик (как в школе)


from logging import exception
from curses.ascii import isdigit

class MyException(Exception):
    pass

def getCalcNumSys(num001, num002, num_cap, operation = '+'):
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    result = str()

    # валидация ввода:
    # 1 - числа должны соответствовать заданной СС
    # 2 - для num001 и num002 допустим только ввод символов из списка symbols
    # 3 - для num_cap только int числа и от 2 до 36
    # 4 - для operation только '+'
    if type(num_cap) is not int or num_cap > 36 or num_cap < 2:
        print('аргумент num_cap функции getCalcNumSys должен быть целым числом от 2 до 36')
        raise MyException(Exception)
    for digit in str(num001) + str(num002):
        if digit not in symbols[0: num_cap]:
            print('аргументы num001 и num002 функции getCalcNumSys должны состоять только из символов от 0-9 A-V '
                  'и не должны выходить за рамки заданной СС')
            raise MyException(Exception)
    if operation not in ['+']:
        print('аргумент operation функции getCalcNumSys должен быть одним из символов: "+"')
        raise MyException(Exception)

    match operation:
        case '+':
            remaind = 0 # учет единицы в старшем разряде
            for i in range(0, max(len(str(num001)), len(str(num002)))):
                try: # для случая когда числа разной длины и для уравнивания требуется добавить нули в меньшее
                    num001_digit = str(num001)[::-1][i]
                except IndexError:
                    num001_digit = '0'
                try:
                    num002_digit = str(num002)[::-1][i]
                except IndexError:
                    num002_digit = '0'
                indx = symbols.index(num001_digit) + symbols.index(num002_digit) + remaind
                if indx >= num_cap:
                    remaind = 1
                    indx = indx % len(symbols) # на случай если индекс суммарного символа выходит за список
                    sum_digits = symbols[indx % num_cap] # остаток, если суммарный символ больше разрядности СС
                else:
                    remaind = 0
                    sum_digits = symbols[indx]
                result = sum_digits + result
            if remaind != 0: # для случая когда единица остается после завершения цикла (например 999 + 1)
                result = str(remaind) + result
            return result

# как тестировал:
# getCalcNumSys(111, '32D', 16)   -------> 43E
# getCalcNumSys('0', '0', 2)      -------> 0
# getCalcNumSys(22, 33, 10)       -------> 55
# getCalcNumSys('999', '1', 10)   -------> 1000
# getCalcNumSys('999', '1', 12)   -------> 99A
# getCalcNumSys('AAA', 'BBB', 16) -------> 1665
# etCalcNumSys('AVA', 'BVB', 36)  -------> MQL
# getCalcNumSys('Z', '1', 36)     -------> 10
# getCalcNumSys('Z', 'Z', 36)     -------> 1Y
# getCalcNumSys('Z', -1, 36)      -------> ошибка (предусмотренная)
# getCalcNumSys('Z', 'Z', 36, 'plus') ---> ошибка
# getCalcNumSys('Z', 'Z', 37)     -------> ошибка
# getCalcNumSys('Z', 'Z', '36')   -------> ошибка
# getCalcNumSys('999', '1', 2)    -------> ошибка
# getCalcNumSys('9+=?9', '13', 10) ------> ошибка


print(getCalcNumSys('A', '-1', 16))