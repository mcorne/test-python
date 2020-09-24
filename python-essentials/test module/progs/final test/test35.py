class X:
    pass

class Y(X):
    pass

class Z(Y):
    pass

x = X()
z = Z()
print(isinstance(x,Z),isinstance(z,X))