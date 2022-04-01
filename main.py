class Lexer:
    symbol = ''

    def __init__(self):
        self.buffer = ""
        self.b_counter = 0
        self.current_state = "S"
        self.end_m = ['+', '-', '*', '/', '^', ')', '(']
        self.functions = ['cos', 'sin', 'tg', 'ctg', 'ln', 'e']
        self.lexem = {'I': self.i_func, 'R': self.r_func, 'E': self.end_func, 'X': self.x_func, 'F': self.f_func,
                      'B': self.b_func, 'U': self.um_func}
        self.comman_h = []
        self.viraz = []
        self.result_viraz = []

    def parse(self, stroka):
        count_b = 0
        viraz_e = []
        for obz in stroka:
            if self.buffer in self.functions:
                self.viraz.append(self.buffer)
                self.buffer = ''
            self.symbol = obz
            self.s_func()
            if len(self.comman_h) != 0 and self.check() == 'Invalid syntax':
                return f'Incorrect write in {self.current_state[-1]} state'
            self.comman_h.append(self.current_state)
            self.lexem.get(self.current_state)()
        self.viraz.append(self.buffer)
        for i in self.viraz:
            if i != '':
                self.result_viraz.append(i)
        for i in self.viraz:
            if i == '(':
                count_b += 1
            elif i == ')':
                count_b -= 1
            if count_b < 0:
                break
            if i != '':
                viraz_e.append(i)
        if count_b != 0:
            return 'Invalid brackets'
        elif viraz_e[-1] != ')' and (viraz_e[-1].isdigit() == False) and viraz_e[-1] != 'x' and viraz_e[-1].count('.') != 1:
            print(self.viraz)
            return 'Invalid end of expression'
        else:
            return self.result_viraz

    def check(self):
        if self.comman_h[-1] == 'I' and (
                self.current_state == 'F' or self.current_state == 'B' or self.current_state == 'X'):
            return 'Invalid syntax'
        elif self.comman_h[-1] == 'R' and (
                self.current_state == 'F' or self.current_state == 'X' or self.current_state == 'B'):
            return 'Invalid syntax'
        elif self.comman_h[-1] == 'B' and self.current_state == 'E':
            if self.symbol != '-':
                return 'Invalid syntax'
        elif self.comman_h[-1] == 'X' and self.current_state != 'E':
            return 'Invalid syntax'
        elif self.comman_h[-1] == 'F' and (
                self.current_state == 'I' or self.current_state == 'R' or self.current_state == 'X' or self.current_state == 'E'):
            return 'Invalid syntax'
        elif self.comman_h[-1] == 'E' and (self.current_state == 'E'):
            if self.viraz[-1] != ')':
                return 'Invalid syntax'
        elif self.comman_h[-1] == 'U' and (self.symbol == ')' or self.current_state == 'E'):
            if self.symbol != '(':
                return 'Invalid syntax'
        else:
            return True

    def s_func(self):
        if self.symbol.isdigit():
            self.current_state = 'I'
        elif self.symbol == '.':
            self.current_state = 'R'
        elif self.symbol == 'x':
            self.current_state = 'X'
        elif self.symbol == 'u':
            self.current_state = 'U'
        elif self.symbol.isalpha():
            self.current_state = 'F'
        elif self.symbol == '(':
            self.current_state = 'B'
        else:
            self.current_state = 'E'

    def i_func(self):
        self.buffer += self.symbol

    def um_func(self):
        self.viraz.append('u')

    def r_func(self):
        self.buffer += self.symbol

    def x_func(self):
        self.buffer += self.symbol

    def f_func(self):
        self.buffer += self.symbol

    def b_func(self):
        self.viraz.append(self.symbol)

    def end_func(self):
        if self.symbol in self.end_m:
            self.viraz.append(self.buffer)
            self.viraz.append(self.end_m[self.end_m.index(self.symbol)])
            self.buffer = ""
