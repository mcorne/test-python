d = { 1:0, 2:1, 3:2, 0:1 }
x = 0
for y in range(len(d)):
    x = d[x]
print(x)