class A:
    pass

class B:
    pass

class C(A,B):
    pass

print(issubclass(C,A) and issubclass(C,B))