class A:
    def __init__(self):
        pass
    def f(self):
        return 1
    def g():
        return self.f()

a = A()
print(a.g())