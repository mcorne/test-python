def f(a, l = []) -> list:
    l.append(a)
    return l

print(f(1))
print(f(2))
print(f(3))
