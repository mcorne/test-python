def I(n):
    s = '+'
    for i in range(n):
        s += s
        yield s
for x in I(2):
    print(x,end='')