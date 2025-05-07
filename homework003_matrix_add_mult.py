# 1. Сложение матриц
# 2. Умножение матриц


# Позволяет пользователю заполнять матрицу построчно.
def get_filled_matrix(mass):

    # возвращает True если матрица заполняется симметрично
    def is_same_amount_valid(lst):
        return amount == len(lst)

    # возвращает True если каждый из элементов списка является числом состоящим из цифр
    def each_list_element_is_digit(lst):
        for el in lst:
            if not el.lstrip("-").isdigit():
                return False
        return True

    # ввод первой строки с длиной которой будут сравниваться все последующие
    while True:
        lst1 = input().split()
        if each_list_element_is_digit(lst1):
            amount = len(lst1) # длина строк матрицы (задается первым вводом)
            break
        else:
            print('Матрица должна состоять только из целых чисел! Повторите ввод первой строки еще раз: ')


    while lst1 != []:
        if is_same_amount_valid(lst1) and each_list_element_is_digit(lst1):
            mass.append(lst1)
        else:
            print('Количество элементов в строке должно быть каждый раз одинаковым и состоять только из целых чисел! '
                  'Продолжите заполнение матрицы, учитывая это.')
        lst1 = input().split()


# Принимает на вход массив и выводит его в виде матрицы
def print_mass_like_matrix(mass):
    for lst in mass:
        for el in lst:
            print(el, end = '\t')
        print()


def get_matrix_addition(matrix1, matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            matrix2[i][j] = int(matrix1[i][j]) + int(matrix2[i][j])
    return matrix2


# возвращает True если сложение валидно
def addition_is_valid(matrix1, matrix2):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        return True
    else:
        return False


def get_matrix_multiplication(matrix1, matrix2):
    matrix_res = [[0 for i in range(len(matrix1))] for j in range(len(matrix2[0]))]
    for i in range(len(matrix_res)):
        for j in range(len(matrix_res[0])):
            for k in range(len(matrix1[0])):
                matrix_res[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])
                # print(matrix1[i][k], '*', matrix2[k][j], '+=' ,matrix_res[i][j])
    return matrix_res


# возвращает True если умножение валидно
def multiplication_is_valid(matrix1, matrix2):
    if len(matrix1) == len(matrix2[0]) and len(matrix1[0]) == len(matrix2):
        return True
    else:
        return False


def operation_is_valid(operation):
    if operation == '+' or operation == '*':
        return True
    else:
        return False

if __name__ == '__main__':
    while True:
        mass1 = []
        print('Введите первую матрицу. Построчно, отделяя каждый элемент пробелом. '
              'По окончании заполнения матрицы введите пустую строку нажатием enter.')
        get_filled_matrix(mass1)
        # print(mass1)

        mass2 = []
        print('Введите вторую матрицу. Построчно, отделяя каждый элемент пробелом. '
              'По окончании заполнения матрицы введите пустую строку нажатием enter.')
        get_filled_matrix(mass2)
        # print(mass2)

        operation = input('Введите операцию (+ или *): ')
        while not operation_is_valid(operation):
            print('Ввод операции должен содержать только один символ (+ или *)! Повторите ввод.')
            operation = input('Введите операцию: ')
        match operation:
            case '+':
                if addition_is_valid(mass1, mass2):
                    print()  # отступ
                    print('#######################################')
                    print_mass_like_matrix(mass1)
                    print('+')
                    print_mass_like_matrix(mass2)
                    print('=')
                    print_mass_like_matrix(get_matrix_addition(mass1, mass2))
                    print('#######################################', '\n')
                else:
                    print('Допускается только сложение матриц одинаковой размерности! Повторите ввод.')
            case '*':
                if multiplication_is_valid(mass1, mass2):
                    print()  # отступ
                    print('#######################################')
                    print_mass_like_matrix(mass1)
                    print('*')
                    print_mass_like_matrix(mass2)
                    print('=')
                    print_mass_like_matrix(get_matrix_multiplication(mass1, mass2))
                    print('#######################################', '\n')
                else:
                    print('Для успешного умножения матриц количество столбцов первой матрицы должно быть равно количеству строк второй!'
                          ' Повторите ввод.')