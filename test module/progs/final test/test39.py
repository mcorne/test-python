class A:
    A = 1
    def __init__(self,v = 2):
        self.v = v + A.A
        A.A += 1

    def set(self,v):
        self.v += v
        A.A += 1
        return 

a = A()
a.set(2)
print(a.v)