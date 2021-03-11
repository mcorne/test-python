MAX = 20
a = list(range(0, MAX + 1))
a[0] = None # barré
a[1] = None
i = 2
length = len(a)

while i < length:
    if a[i]:
        j = i
        p = None
        while j < length:
            if a[j]:
                if not p:
                    p = a[j]
                    print(p)
                elif not a[j] % p:
                    a[j] = None
            j += 1
    i += 1

print(a)
