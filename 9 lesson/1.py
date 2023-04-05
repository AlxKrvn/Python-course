def open_my_file(x):
    with open(x) as file_1:
        print(file_1.read())

open_my_file('1.txt')
