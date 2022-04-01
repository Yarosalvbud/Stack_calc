from main import*
from Poland import*
from Polandback import*
from Chisl import*
from integral import Integral

parser = Lexer()
pol = Poland()
pol_b = Stack_calk()
print('Введите выражение')
stroka = input()
stroka = stroka.replace(' ', '')
stroka = parser.parse(stroka)
try:
    stroka = pol.parse(stroka)
except:
    print(stroka)
    exit()
if 'x' not in stroka:
    print(stroka)
    try:
        try:
            stroka = pol_b.parse(stroka)
        except:
            stroka = stroka[0:-1]
    except:
        print('Incorrect Write')
else:
    print('Вы хотите найти значение x?')
    if input() == 'Да':
        print('Введите стартовое значение')
        a = int(input())
        print('Введите конечное значение')
        b = int(input())
        f_x = inequality(a, b, stroka)
        try:
            print(f_x.find())
        except:
            print('Нет корней на данном отрезке')
    else:
        print('Введите стартовое значение')
        a = int(input())
        print('Введите конечное значение')
        b = int(input())
        i_x = Integral(a, b, stroka)
        try:
            print(i_x.find_integral())
        except:
            print('Невозможно вычислить интеграл на данном отрезке')

