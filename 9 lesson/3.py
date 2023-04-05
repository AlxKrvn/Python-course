def numbers_to_file(x):
    with open(x) as file_r:
        with open('2.txt', 'x') as file_w:
            for i in file_r.read():
                if i.isdigit():
                    file_w.write(i)

file = '1.txt'
numbers_to_file(file)

