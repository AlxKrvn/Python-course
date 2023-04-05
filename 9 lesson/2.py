import os

def contents(way_to_file):
    s = os.listdir(way_to_file)
    return s

way = 'C://Users/Alex/Desktop/PYTHON (курс)/Python-course'

print(contents(way))