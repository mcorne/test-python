try:
    raise Exception
except BaseException:
    print("a",end='')
else:
    print("b",end='')
finally:
    print("c")