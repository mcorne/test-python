def I(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s
for x in I(3):
    print(x,end='')