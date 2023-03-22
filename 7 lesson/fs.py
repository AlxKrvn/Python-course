def summ(a, b):
    if a > b:
        a, b = b, a
    c = 0
    for i in range(a, b+1):
        c += i
    return(c)
print(summ(int(input()), int(input())))