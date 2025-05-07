# 3. Вывод матрицы по спирали. На вход принимает N = 5, заполняет матрицу от 1 до 25
# 3.1. По часовой
# 3.2 Против часовой

from homework003_matrix_add_mult import print_mass_like_matrix

def fill_mass_el_left_to_right(curr_row, curr_column, mass):
    i = 0
    global current_number
    try:
        while mass[curr_row][curr_column +i] == 0:
            mass[curr_row][curr_column +i] = current_number
            i += 1
            current_number += 1
    except IndexError:
        return curr_row, curr_column +i -1 # -1 потому что значение уже превысило допустимый индекс (и накинуло ошибку)
    finally:
        return curr_row, curr_column +i -1

def fill_mass_el_up_to_down(curr_row, curr_column, mass):
    i = 0
    global current_number
    try:
        while mass[curr_row +i][curr_column] == 0:
            mass[curr_row +i][curr_column] = current_number
            i += 1
            current_number += 1
    except IndexError:
        return curr_row +i -1, curr_column
    finally:
        return curr_row +i -1, curr_column

def fill_mass_el_right_to_left(curr_row, curr_column, mass):
    i = 0
    global current_number
    try:
        while mass[curr_row][curr_column +i] == 0:
            mass[curr_row][curr_column +i] = current_number
            i -= 1
            current_number += 1
    except IndexError:
        return curr_row, curr_column +i +1
    finally:
        return curr_row, curr_column +i +1

def fill_mass_el_down_to_up(curr_row, curr_column, mass):
    i = 0
    global current_number
    try:
        while mass[curr_row +i][curr_column] == 0:
            mass[curr_row +i][curr_column] = current_number
            i -= 1
            current_number += 1
    except IndexError:
        return curr_row +i +1, curr_column
    finally:
        return curr_row +i +1, curr_column



if __name__ == '__main__':
    while True:
        current_number = 1
        matrix_size = input('Введите размерность матрицы: ')
        if matrix_size.isdigit():
            matrix_size = int(matrix_size)
        else:
            print('Размерность матрицы должна задаваться целым положительным числом!')
            continue

        matrix1 = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
        row = 0
        column = -1 # -1 для того чтобы функция в цикле сработала при первой итерации
        while current_number <= matrix_size**2:
            row, column = fill_mass_el_left_to_right(row, column +1, matrix1)
            row, column = fill_mass_el_up_to_down(row +1, column, matrix1)
            row, column = fill_mass_el_right_to_left(row, column -1, matrix1)
            row, column = fill_mass_el_down_to_up(row -1, column, matrix1)

        print()
        print_mass_like_matrix(matrix1)
        print()

