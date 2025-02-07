# найти количество четных цифр в числе
# пробую добавить рекурсию
res = 0
def digit_counter_recursion(number):
    global res
    if number // 10 == 0:
        return res
    res += 1
    return digit_counter_recursion(number // 10)

#print(digit_counter_recursion(9933))
#print(digit_counter_recursion(9933))


# написать алгоритм разворачивающий число (было "123" стало "321")
# за два цикла
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

#print(reverse_number(98666076))

# попробовать поменять две переменных местами
a = 223
b = 564
c = a
a = b
b = c
#print(a,b)
a = 111
b = 222
a = a + b
b = a - b
a = a - b
#print(a, b)
a = 10
b = 20
a, b = b, a
#print(a, b)