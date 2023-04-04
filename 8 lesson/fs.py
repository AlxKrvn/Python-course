def multi_1(factor, list):  # умножение элемента на число
    return [i * factor for i in list]
def multi_2(list):    # произведение элементов
    result = 1
    for i in list:
        result *= i
    return result
f = int(input('factor = '))    # коэффициент
n = int(input('count = '))    # кол-во элементов в списке
l = [int(input()) for i in range(n)]
print(multi_1(f, l))
print(multi_2(l))




