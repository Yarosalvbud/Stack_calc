
class Poland:

    def __init__(self):
        self.stack = []
        self.deck = []
        self.current_status = 'N'
        self.symbol = ''
        self.functions = {'B': self.bracket, 'S': self.cycle, 'I': self.integer, 'Z': self.z_status}
        self.priority = {'+': 2, '-': 2, '(': 1, '*': 3, '/': 3, '^': 3, 'sin': 4, 'ln': 4, 'cos': 4, 'tg': 4, 'ctg': 4,
                         'e': 4, 'u':2}
        self.stroka = []

    def parse(self, stroka):
        self.stroka = stroka.copy()
        for ob in stroka:
            self.symbol = ob
            self.status()
            self.functions.get(self.current_status)()
            self.stroka.remove(ob)
        for i in self.stack:
            self.deck.append(i)
        return self.deck

    def status(self):
        if self.symbol == '(':
            self.current_status = 'B'
        elif self.symbol == ')':
            self.current_status = 'S'
        elif self.symbol.isdigit() or self.symbol == 'x' or self.symbol.count('.') == 1:
            self.current_status = 'I'
        else:
            self.current_status = 'Z'

    def bracket(self):
        self.stack.insert(0, self.symbol)

    def cycle(self):
        for ob in self.stack:
            if self.stack.index('(') < self.stack.index(ob):
                break
            if ob != '(':
                self.deck.append(ob)
                self.stack.pop(0)
            else:
                break
        if '(' in self.stack:
            self.stack.remove('(')

    def integer(self):
        self.deck.append(self.symbol)

    def z_status(self):
        status_1 = self.priority.get(self.symbol)
        if len(self.stack) > 0:
            status_2 = self.priority.get(self.stack[0])
        else:
            status_2 = 0
        if len(self.stack) == 0 or status_1 > status_2:
            self.stack.insert(0, self.symbol)
        else:
            while status_2 >= status_1:
                if len(self.stack) > 0:
                    self.deck.append(self.stack[0])
                    self.stack.pop(0)
                if len(self.stack) > 0:
                    status_2 = self.priority.get(self.stack[0])
                else:
                    status_2 = 0
            self.stack.insert(0, self.symbol)