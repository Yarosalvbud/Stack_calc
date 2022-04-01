import math


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, c):
        self.stack.insert(0, c)

    def pop(self):
        return self.stack.pop(0)

    def show(self):
        return self.stack


class Stack_calk:
    def __init__(self):
        self.stack = Stack()
        self.symbol = ''
        self.current_status = ''
        self.n = ['+', '-', '*', '/', '^']
        self.functions = {'I': self.integer, 'T': self.two, 'F': self.function, 'Fb': self.fbx, 'U':self.u_state}

    def parse(self, stroka):
        for ob in stroka:
            self.symbol = ob
            self.status()
            self.functions.get(self.current_status)()
        return self.stack.show()

    def status(self):
        if self.symbol.isdigit():
            self.current_status = 'I'
        elif self.symbol in self.n:
            self.current_status = 'T'
        elif self.symbol == 'u':
            self.current_status = 'U'
        elif self.symbol.count('.') == 1:
            self.current_status = 'Fb'
        else:
            self.current_status = 'F'

    def integer(self):
        self.stack.push(int(self.symbol))

    def u_state(self):
        first = self.stack.pop()
        self.stack.push(-first)

    def fbx(self):
        self.stack.push(float(self.symbol))

    def two(self):
        second = self.stack.pop()
        first = self.stack.pop()
        if self.symbol == '+':
            self.stack.push(first + second)
        elif self.symbol == '*':
            self.stack.push(first * second)
        elif self.symbol == '/':
            self.stack.push(first / second)
        elif self.symbol == '-':
            self.stack.push(first - second)
        elif self.symbol == '^':
            self.stack.push(first ** second)

    def function(self):
        digit = self.stack.pop()
        if self.symbol == 'cos':
            self.stack.push(math.cos(digit))
        elif self.symbol == 'sin':
            self.stack.push(math.sin(digit))
        elif self.symbol == 'tg':
            self.stack.push(math.sin(digit) / math.cos(digit))
        elif self.symbol == 'ctg':
            self.stack.push(math.cos(digit) / math.sin(digit))
        elif self.symbol == 'ln':
            self.stack.push(math.log(digit))
        elif self.symbol == 'e':
            self.stack.push(math.exp(digit))
