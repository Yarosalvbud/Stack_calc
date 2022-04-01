import math
from Polandback import Stack_calk

class inequality:
    def __init__(self, a, b, stroka):
        self.a = a
        self.b = b
        self.E = 0.001
        self.stroka = stroka

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

    def find(self):
        x = self.b - (self.f(self.b) / (self.f(self.b) - self.f(self.a))) * (self.b - self.a)
        while abs(self.f(x)) > self.E:
            x = self.b - (self.f(self.b) / (self.f(self.b) - self.f(self.a))) * (self.b - self.a)
            if abs(self.a - x) < abs(self.b - x):
                self.a = x
            else:
                self.b = x
        return x





