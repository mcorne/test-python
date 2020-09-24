str =  'abcdef'
def fun(s):
    del s[2]
    return s

print(fun(str))