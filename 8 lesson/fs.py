a = [1, 3, 2, 4, 5, 19]
b = []
def pr(a, x):
    for i in a:
        b += [i*x]
    return(b)
print(pr(a, int(input())))