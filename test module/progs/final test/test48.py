def a(x):
    def b():
        return x + x
    return b

x = a('x')
y = a('')
print(x() + y())