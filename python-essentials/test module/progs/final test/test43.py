class A:
    def __init__(self,v):
        self._a = v + 1

a = A(0)
print(a._a) # not private, __a would be private
