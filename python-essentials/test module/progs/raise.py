def badfun(n):
    raise ZeroDivisionError

try:
    badfun(1)
except ArithmeticError:
    print('what is that?')
