def compare(list1, list2):
    for i in list1:
        if i in list2:
            print(True)
            break

a = [input() for i in range(int(input('count = ')))]
b = [input() for i in range(int(input('count = ')))]

compare(a, b)