# найти количество цифр в числе (задача которую обсуждали на созвоне)
# мой вариант решения
# как тестил:
# [0] -> 1
# [1] -> 1
# [7] -> 1
# [25] -> 2
# [1111] -> 4
# [2000] -> 4
# [20007] -> 5
# [120003219313] -> 12
def get_digits_count_v1(number):
    i = 0
    ans = -1
    while ans != 0:
        i += 1
        ans = number // 10**i
    return i
#print(getDigitsCount_v1(0))


# найти количество цифр в числе
# (алгоритм который проговорили на занятии)
# не работает при number = 0 (нужен цикл с пост-условием?)
# как тестил:
# [0] -> 0
# [1] -> 1
# [7] -> 1
# [25] -> 2
# [1111] -> 4
# [2000] -> 4
# [20007] -> 5
# [120003219313] -> 12
def get_digits_count_v2(number):
    res = 0
    while number != 0:
        number = number // 10
        res += 1
    return res
#print(getDigitsCount_v2(0))


# найти количество четных цифр в числе
# не работает при number = 0
# как тестил:
# [0] -> 0
# [1] -> 0
# [6] -> 1
# [359] -> 0
# [468] -> 3
# [583] -> 1
# [888] -> 3
# [1000] -> 3
# [10001] -> 3
def get_even_digits_count(number):
    res = 0
    while number != 0:
        digit = number % 10
        if digit % 2 == 0:
            res += 1
        number = number // 10
    return res
#print(getEvenDigitsCount(23231))


# найти количество цифр которые делятся на 3 и не делятся на 2
# как тестил:
# [0] -> 0
# [1] -> 0
# [3] -> 1
# [69] -> 1
# [333] -> 3
# [735] -> 1
# [1000] -> 0
# [3000] -> 1
# [50009] -> 1
foo = lambda n: n % 2 != 0 and n % 3 == 0
def count_odd_multiple_three(number):
    res = 0
    while number != 0:
        digit = number % 10
        if foo(digit):
            res += 1
        number = number // 10
    return res
# print(count_odd_multiple_three(32424169))

# написать алгоритм разворачивающий число (было "123" стало "321")
# написал за два цикла (можно ли за 1?)
# как тестил:
# [0] -> 0
# [1] -> 1
# [23] -> 32
# [555] -> 555
# [900] -> 9
# [9002] -> 2009
def reverse_number(number):
    list_of_digits = list()
    i = int()
    result = int()
    while number != 0:
        last_digit = number % 10
        number = number // 10
        list_of_digits.append(last_digit)
        i += 1
    for digit in list_of_digits:
        i -= 1
        result += digit * 10**i
    return result

# алгоритм разворачивающий число (было "123" стало "321")
# но без использования вспомогательных структур данных
def get_reverse_number(number):
    result = 0
    while number != 0:
        result = result * 10 + number % 10
        number //= 10
    return result

print(get_reverse_number(11123130009))


# найти максимальную цифру в числе
# как тестил:
# [0] -> (0, 0)
# [1] -> (1, 1)
# [28] -> (8, 2)
# [999] -> (9, 9)
# [3000] -> (3, 0)
# [30001] -> (3, 0)
def get_max_digit(number):
    max = number % 10
    while number != 0:
        digit = number % 10
        if digit > max:
            max = digit
        number //= 10
    return max

# найти минимальную цифру в числе
def get_min_digit(number):
    min = number % 10
    while number != 0:
        digit = number % 10
        if digit < min:
            min = digit
        number //= 10
    return min
# print(getMinDigit(572), getMaxDigit(572))


# напиши функцию которая выводит все простые числа от 0 до 10000
# не уверен что использование среза (slice) - удачное решение
def get_prime_numbers_10k_v1():
    prime_list = [1, 2]
    counter = 0 # для проверки количества заходов в цикл
    for number in range(3, 10001):
        for sub in prime_list[1:]:
            counter += 1
            if number % sub == 0:
                break
        else:
            prime_list.append(number)
    # print(counter)
    return prime_list
get_prime_numbers_10k_v1()

# вывод всех простых чисел от 0 до 10000 по алгоритму Эратосфена
def get_prime_numbers_10k_v2():
    last_number = 10000
    list_of_numbers = list(i for i in range(2, last_number+1))
    i = 1 # счетчик внешнего цикла
    p = 2 # число, кратные которому вычеркиваются из списка
    num = p**2
    counter = 0 # для проверки количества заходов в цикл (чтобы сравнить с первой версией алгоритма)
    while p**2 <= last_number:
        j = 0 # счетчик вложенного цикла
        while num <= last_number:
            num = p * (p + j)
            if num in list_of_numbers:
                list_of_numbers.remove(num)
            j += 1
            counter += 1
        p = list_of_numbers[i] # первое невычеркнутое и непроверенное число в списке
        num = list_of_numbers[i]
        i += 1
    # print(counter)
    return list_of_numbers
# print(len(getPrimeNumbers10k_v2()))
print(get_prime_numbers_10k_v2())