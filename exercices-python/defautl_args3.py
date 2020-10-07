def f(a, l = []) -> list:
    l.append(a)
    return l

b = []
b = f(1, b)
b = f(2, b)
b = f(3, b)
print(b)
