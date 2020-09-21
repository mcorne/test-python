
try:
    a = int(input('a: '))
    b = int(input('b: '))
    print(a/b)
except ZeroDivisionError:
    print('Cannot divide by zero!')
except ArithmeticError:
    print('Need integer value!')
except:
    print('Oh, dear!')
print('The end')