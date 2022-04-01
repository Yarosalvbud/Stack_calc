import math
from Polandback import Stack_calk

class Integral:
    def __init__(self, a, b, stroka):
        self.a = a
        self.b = b
        self.stroka = stroka
        self.go = 0.00001

    def f(self, chisl):
        parse = []
        for i in self.stroka:
            if i == 'x':
                if chisl > 0:
                    parse.append(str(chisl))
                else:
                    parse.append(str(abs(chisl)))
                    parse.append('u')
            else:
                parse.append(i)
        x = Stack_calk()
        y = x.parse(parse)
        return y[0]

    def find_integral(self):
        a_new = self.a + self.go
        square = 0
        while self.a <= self.b:
            square += ((a_new - self.a) / 6) * (self.f(self.a) + 4 * self.f((self.a + a_new) / 2) + self.f(a_new))
            self.a = a_new
            a_new += self.go
        return square



