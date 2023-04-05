""" 
Написать программу с классом Студент, у которого будет 3 атрибута: имя, номер и возраст. Необходимо создать пять методов: 

- для получения данных об имени студента;

- для получения данных о возрасте;

- для номера студента;

- для изменения данных возраста;

- для изменения данных группы. 

"""
class Stud():

    def __init__(self, name = '', num = '', age = 0):
        self.name = name
        self.num = num
        self.age = age

    def num_dif(self):
        self.num = input()
    
    def age_dif(self):
        self.age = int(input())
    
stud1 = Stud('Alex', '12-C-1', 19)
print(f'имя студента {stud1.name}\nгруппа № {stud1.num}\nполных лет {stud1.age}')

stud1.num_dif()
stud1.age_dif()
print(f'имя студента {stud1.name}\nгруппа № {stud1.num}\nполных лет {stud1.age}')

