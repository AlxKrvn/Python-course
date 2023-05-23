# объявление функции
def cool_password(p):
    a, b, c = 0, 0, 0
    
    if len(p) < 8:
        return False
    for i in p:

        if i.isdigit():
            a += 1
        
        elif i.isalpha():
            if i.islower():
                b += 1
            else:
                c += 1
    
    if 0 < a < (len(p) -2) and 0 < b < (len(p) - 2) and 0 < c < (len(p) - 2):
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(cool_password(txt))

    
            

