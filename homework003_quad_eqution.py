from curses.ascii import isdigit
import re, math

import matplotlib
import matplotlib.pyplot as plt



def get_members(equation_list, current_number):
    is_a_coeff_growing = False
    is_b_coeff_growing = False
    a = 0
    b = 0
    c = 0

    for i in range(len(equation_list)):
        if equation_list[i] == "x" and equation_list[i-1] == "^":
            is_a_coeff_growing = True
        elif (equation_list[i] == "x" and equation_list[i-1]
              != "^"):
            is_b_coeff_growing = True
        elif equation_list[i] == "2" and equation_list[i+1] == "^":
            continue
        elif equation_list[i] == "+":
            # проверка на случай когда перед x или x^2 нет коэффициента (он должен быть равен 1)
            if len(current_number) == 0:
                coeff = 1
            else:
                coeff = int(''.join(current_number))

            if is_a_coeff_growing:
                a += coeff
            elif is_b_coeff_growing:
                b += coeff
            else:
                c += coeff
            current_number.clear()
            is_a_coeff_growing = False
            is_b_coeff_growing = False
        elif equation_list[i] == "-":
            if len(current_number) == 0:
                coeff = -1
            else:
                coeff = int('-' + ''.join(current_number))

            if is_a_coeff_growing:
                a += coeff
            elif is_b_coeff_growing:
                b += coeff
            else:
                c += coeff
            current_number.clear()
            is_a_coeff_growing = False
            is_b_coeff_growing = False
        # если символ - цифра, то он добавляется в массив
        elif isdigit(equation_list[i]):
            current_number.insert(0, equation_list[i])
        # случай когда коэффициент после прогона строки остался не добавленным
        elif equation_list[i] == '$' and equation_list[i - 1] != '-':
            if is_a_coeff_growing:
                if len(current_number) == 0:
                    a += 1
                else:
                    a += int(''.join(current_number))
            elif is_b_coeff_growing:
                if len(current_number) == 0:
                    b += 1
                else:
                    b += int(''.join(current_number))
            else:
                coeff = int(''.join(current_number))
                c += coeff
                current_number.clear()
        else:
            continue
    current_num_list.clear()
    return a, b, c


def get_equation_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    # print(discriminant)
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return


def is_equation_valid(equation):
    if not re.fullmatch(r'^[\dx\^+\-=.]+$', equation):
        print('Введены недопустимые символы!')
        return False
    elif any(i in equation for i in ['--', '++', '+-', '-+']):
        print('В уравнении не должно быть подряд несколько символов "+" и "-"!')
        return False
    elif equation.count('=') != 1:
        print('Уравнение должно иметь символ "=" и встречаться он должен единожды!')
        return False
    elif 'x^2' not in equation:
        print('Квадратное уравнение должно содержать "x^2"!')
        return False
    # если есть символ "^" то после него должен стоять символ "2", в то же время после "2" не должна стоять цифра
    elif re.search(r'\^(?!2(?!\d))', equation):
        print('Символ "^" допустимо использовать только в связке с "2" (x^2)!')
        return False
    else:
        return True


if __name__ == '__main__':
    current_num_list = []
    equation_right_part = []
    equation_left_part = []


    # equation = '4x^2-x^2+6x-2=22-13-x^2+5x'   # переменная для тестов (без задания через консоль)
    equation = input('Введите квадратное уравнение (пример: 23x^2+32x+1=0): ')
    equation = equation.replace(' ', '')

    # валидация
    while not is_equation_valid(equation):
        equation = input('Повторите ввод! (пример: 23x^2+32x+1=0): ')

    # реверс массива из символов правой части уравнения (+ дополнение символов в конец и начало)
    for i in range(len(equation) - 1, -1, -1):
        if equation[i] == '=':
            break
        equation_right_part.append(equation[i])
    equation_right_part.append("$")  # для избежания ошибки по индексу
    equation_right_part.insert(0, "#")  # -//-
    # то же самое для левой части уравнения
    for i in range(len(equation)):
        if equation[i] == '=':
            break
        equation_left_part.insert(0, equation[i])
    equation_left_part.append("$")  # для избежания ошибки по индексу
    equation_left_part.insert(0, "#")  # -//-

    a_left, b_left, c_left = get_members(equation_left_part, current_num_list)
    a_right, b_right, c_right = get_members(equation_right_part, current_num_list)
    a = a_left - a_right
    b = b_left - b_right
    c = c_left - c_right

    roots = None
    if a != 0:
        roots = get_equation_roots(a, b, c)

    print('#########################')
    if roots != None and len(roots) == 2:
        print('Квадратное уравнение', equation, 'имеет два корня:',
              'x1 =', f"{roots[0]:.2f}", 'x2 =', f"{roots[1]:.2f}")
    elif roots != None and len(roots) == 1:
        print('Квадратное уравнение', equation, 'имеет один корень:',
              'x1 =', f"{roots:.2f}")
    else:
        print('Квадратное уравнение', equation, 'не имеет корней')
    print('#########################')


    # отображение графика
    x = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = []
    for x1 in x:
        y1 = a * x1**2 + b * x1 + c
        y.append(y1)
    plt.plot(x, y)
    plt.xlabel('Ось х')
    plt.ylabel('Ось y')
    plt.title(equation)
    plt.grid()
    plt.show()