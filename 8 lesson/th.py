a = [1, 6554, 3345, 5, 6]
b = [1, 3, 65, 889]
def sravni(a, b):
    for i in a:
        for j in b:
            if i == j:
                print(True)
        break
        print(False)
print(sravni(a, b))