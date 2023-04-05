#  Написать программу с классом One и создать два атрибута a и b . Написать 4 метода (умножение, сложение, деление и вычитание). Необходимо выполнить эти действия при передаче в методы параметров a и b.

class One():
    a = 0.0
    b = 0.0
    def plus(self):
        c = self.a + self.b
        return c
    def minus(self):
        c = self.a - self.b
        return c
    def star(self):
        c = self.a * self.b
        return c
    def slash(self):
        c = self.a / self.b
        return c
    
first_pair = One()
first_pair.a = float(input('a = '))
first_pair.b = float(input('b = '))
print(f'сумма равна {first_pair.plus()}\nразность равна {first_pair.minus()}\nпроизведение равно {first_pair.star()}\nчастное равно {first_pair.slash()}')