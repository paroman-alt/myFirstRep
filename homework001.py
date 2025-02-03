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
def digit_counter_my_version(number):
    i = 0
    ans = 1
    while ans >= 1:
        i += 1
        ans = number // 10**i
    return i

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
def digit_counter(number):
    res = 0
    while number != 0:
        number = number // 10
        res += 1
    return res

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
def even_digit_counter(number):
    res = 0
    while number != 0:
        digit = number % 10
        if digit % 2 == 0:
            res += 1
        number = number // 10
    return res

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
def odd_multiple_three(number):
    res = 0
    while number != 0:
        digit = number % 10
        if digit % 2 != 0 and digit % 3 == 0:
            res += 1
        number = number // 10
    return res

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

# найти максимальную и минимальную цифры в числе
# как тестил:
# [0] -> (0, 0)
# [1] -> (1, 1)
# [28] -> (8, 2)
# [999] -> (9, 9)
# [3000] -> (3, 0)
# [30001] -> (3, 0)
def max_min_digits(number):
    max = int()
    min = number % 10
    while number != 0:
        digit = number % 10
        if digit > max:
            max = digit
        if digit < min:
            min = digit
        number //= 10
    return max, min

# напиши функцию которая выводит все простые числа от 0 до 10000
def prime_numbers_10k():
    prime_list = [1, 2]
    for number in range(3, 10001):
        was_break = False
        for sub in range(2, number):
            if number % sub == 0:
                was_break = True
                break
        if not was_break:
            prime_list.append(number)
    return prime_list



#print(digit_counter_my_version(120003219313))
#print(digit_counter(2002))
#print(even_digit_counter(10001))
#print(odd_multiple_three(10003))
#print(reverse_number(9002))
#print(max_min_digits(777))
#print(prime_numbers_10k())